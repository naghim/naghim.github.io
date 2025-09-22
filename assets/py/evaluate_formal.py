k='package'
j='language'
i='stdout'
h='encoding'
g='stdin'
f='command'
e='--check'
d='cases'
a='verify'
Z='prepare'
Y='find'
X='cwd'
W='utf-8'
V='languageCommand'
U='arguments'
T=open
P='setup'
O=True
N=None
M='testType'
K='root'
I='output'
H='inputType'
E='input'
D='name'
B=print
from enum import Enum as Q
import tempfile as R,subprocess as F,multiprocessing as l,copy,sys as J,os as A
class G(Q):FILE=0;CONSOLE=1
class S(Q):TEST_EQUAL=0
class L(Q):PYTHON=0;CPP=1
m='q0 q1 q2\n0 1\nq0\nq0\nq0 0 q2\nq0 1 q1\nq1 0 q2\nq1 1 q0\nq2 0 q1\nq2 1 q2'
n='IGEN\nNEM\nIGEN\nIGEN\nNEM'
o='q0 q1 q2\na b\nq0\nq1 q2\nq0 a q1\nq1 a q1\nq1 b q2\nq2 b q2'
p='IGEN\nIGEN\nNEM\nNEM\nIGEN\nIGEN\nNEM\nNEM'
q=[{D:'Problem 1 (DFA - Deterministic Finite Automaton)',d:[{D:'Case 1',H:G.FILE,M:S.TEST_EQUAL,E:m,I:n,U:[e,'10101,111,111110111010101,001,0021']},{D:'Case 2',H:G.FILE,M:S.TEST_EQUAL,E:o,I:p,U:[e,'a,aa,abab,bbb,aaaaaaaaaaaab,aaaaabbbbb,aaaabbbbba,c']}]}]
class C(Exception):0
def b():return A.path.join(R._get_default_tempdir(),next(R._get_candidate_names()))
def r(environment,case):
	B=case;A=environment;C=copy.deepcopy(A[V]);D=B.get(U,[])
	if B[H]==G.FILE:C.extend(['--input',A[E],'--output',A[I]])
	if B[H]==G.CONSOLE:F=B[E]+'\n';J=W
	else:F=N;J=N
	if D:C.extend(D)
	A[f]=C;A[g]=F;A[h]=J
def s(environment,case):
	A=environment;r(A,case)
	try:
		D=F.run(A[f],cwd=A[X],capture_output=O,text=O,input=A[g],encoding=A[h])
		if D.returncode!=0:B(J.stderr);raise C(f"Program exited with status code {D.returncode}")
		A[i]=D.stdout.strip()
	except F.CalledProcessError as E:raise C(f"Couldn't run project: {E}")
def t(folder):
	for(B,G,C)in A.walk(folder):
		for D in C:
			if D=='__main__.py':E=A.path.dirname(B);F=A.path.basename(B);return{j:L.PYTHON,K:E,k:F}
def u(folder):
	for(B,E,C)in A.walk(folder):
		for D in C:
			if D=='CMakeLists.txt':return{j:L.CPP,K:B}
def v(folder):
	for(C,G,D)in A.walk(folder):
		for E in D:
			B=A.path.join(C,E)
			try:
				with T(B,'rb')as F:
					if F.read(4)==b'\x7fELF':return B
			except:pass
def w(environment):A=environment;B=A[k];A[X]=A[K];A[V]=['python3','-m',B]
def x(environment):
	B=environment;A=R.mkdtemp()
	try:F.run(['cmake','-DCMAKE_BUILD_TYPE=Release',B[K]],cwd=A,check=O)
	except F.CalledProcessError as E:raise C(f"Could not configure CMake project")
	try:F.run(['make','-j',str(l.cpu_count())],cwd=A)
	except F.CalledProcessError as E:raise C(f"Could not build CMake project")
	D=v(A)
	if not D:raise C(f"Couldn't find built executable in CMake project")
	B[X]=A;B[V]=[D]
def y(case,environment):
	A=environment;B=b();C=b();A[E]=B;A[I]=C
	with T(B,'w',encoding=W)as D:D.write(case[E])
def z(case,environment):
	D=environment;F=D[E];B=D[I]
	if not A.path.exists(B):raise C(f"Output file not created by program")
	with T(B,'r',encoding=W)as G:H=G.read().strip()
	if not c[case[M]](case,H):raise C(f"Output mismatch: expected different output in file")
	if A.path.exists(F):A.remove(F)
	if A.path.exists(B):A.remove(B)
def A0(case,environment):
	if not c[case[M]](case,environment[i]):raise C(f"Output mismatch: expected different output on stdout")
def A1(case,output):return output.strip()==case[I].strip()
A2={L.PYTHON:{D:'Python',Y:t,Z:w},L.CPP:{D:'CMake (C++)',Y:u,Z:x}}
A3={G.FILE:{P:y,a:z},G.CONSOLE:{P:N,a:A0}}
c={S.TEST_EQUAL:A1}
def A4():
	R=A.getcwd();E=N
	for(S,G)in A2.items():
		E=G[Y](R)
		if E:break
	if not E:B("❌ Couldn't find any project in the current folder ❌");J.exit(1)
	B(f"Found {G[D]} project in {E[K]}")
	try:G[Z](E)
	except C as I:B(f"❌ Error during build: {I}");J.exit(2)
	B('Running tests...');M=False
	for Q in q:
		B(f"Problem: {Q[D]}")
		for F in Q[d]:
			B(f"Running case: {F[D]}")
			try:
				L=A3[F[H]]
				if L[P]:L[P](F,E)
				s(E,F)
				if F[H]:L[a](F,E)
			except C as I:B(f"❌ Failed {F[D]}: {I} ❌");M=O;continue
			B(f"🎉 {F[D]} succeeded 🎉")
	if M:B('❌ Some tests failed. ❌');J.exit(3)
	B('🎉 All tests passed! Congratulations! 🎉');J.exit(0)
if __name__=='__main__':A4()
