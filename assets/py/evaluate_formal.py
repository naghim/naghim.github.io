o='package'
n='language'
m='stdout'
l='encoding'
k='stdin'
j='command'
i='--check'
h='cases'
g='enabled'
f='s0 s1 s2 s3\n0 1\ns0\ns2\ns0 0 s1\ns0 1 s3\ns1 0 s3\ns1 1 s2\ns2 0 s0\ns2 1 s2\ns3 0 s3\ns3 1 s0'
b='verify'
a='prepare'
Z='find'
Y='cwd'
X='utf-8'
W='\n'
V='languageCommand'
U='arguments'
T=open
P='setup'
O=None
N='testType'
K='root'
J=True
I='output'
H='inputType'
E='input'
D='name'
B=print
from enum import Enum as Q
import tempfile as R,subprocess as F,multiprocessing as p,copy,sys as L,os as A
class G(Q):FILE=0;CONSOLE=1
class S(Q):TEST_EQUAL=0
class M(Q):PYTHON=0;CPP=1
q='q0 q1 q2\n0 1\nq0\nq0\nq0 0 q2\nq0 1 q1\nq1 0 q2\nq1 1 q0\nq2 0 q1\nq2 1 q2'
r='IGEN\nNEM\nIGEN\nIGEN\nNEM'
s='q0 q1 q2\na b\nq0\nq1 q2\nq0 a q1\nq1 a q1\nq1 b q2\nq2 b q2'
t='IGEN\nIGEN\nNEM\nNEM\nIGEN\nIGEN\nNEM\nNEM'
A9='q0 q1 q2\n0 1\nq0\nq2\nq0 0 q1\nq0 0 q2\nq0 1 q1\nq1 0 q2\nq1 1 q2'
AA='s0 s1 s2 s3\n0 1\ns0\ns1 s3\ns0 0 s1\ns0 1 s2\ns1 0 s3\ns1 1 s3\ns2 0 s3\ns2 1 s3'
AB='q0 q1 q2\n0 1\nq0\nq2\nq0 0 q0\nq0 0 q1\nq0 1 q0\nq0 1 q1\nq1 0 q1\nq1 0 q2\nq1 1 q0\nq1 1 q1\nq1 1 q2\nq2 0 q1'
AC='s0 s1 s2\n0 1\ns0\ns2\ns0 0 s1\ns0 1 s1\ns1 0 s2\ns1 1 s2\ns2 0 s2\ns2 1 s2'
AD='q0 q1 q2 q3\n0 1\nq0\nq1 q3\nq0 0 q2\nq0 1 q1\nq1 0 q1\nq1 1 q2\nq1 1 q3\nq2 1 q2\nq3 0 q2\nq3 0 q3\nq3 1 q2'
AE='s0 s1 s2 s3\n0 1\ns0\ns2 s3\ns0 0 s1\ns0 1 s2\ns1 1 s1\ns2 0 s2\ns2 1 s3\ns3 0 s3\ns3 1 s1'
AF='q0 q1\n0 1\nq0\nq1\nq0 0 q0\nq0 1 q1\nq1 0 q0\nq1 1 q1'
AG='s0 s1\n0 1\ns0\ns1\ns0 0 s0\ns0 1 s1\ns1 0 s0\ns1 1 s1'
AH='q0 q1 q2 q3 q4 q5\n0 1\nq0\nq2\nq0 0 q1\nq0 1 q4\nq1 0 q4\nq1 1 q2\nq2 0 q0\nq2 1 q2\nq3 0 q5\nq3 1 q4\nq4 0 q4\nq4 1 q3\nq5 0 q4\nq5 1 q2'
AI='s0 s1 s2 s4\n0 1\ns0\ns2\ns0 0 s1\ns0 1 s4\ns1 0 s4\ns1 1 s2\ns2 0 s0\ns2 1 s2\ns4 0 s4\ns4 1 s0'
AJ=f
AK='q0 q1 q2 q3\n0 1\nq0\nq2\nq0 0 q1\nq0 1 q3\nq1 0 q3\nq1 1 q2\nq2 0 q0\nq2 1 q2\nq3 0 q3\nq3 1 q0'
AL=f
AM='q0 q1 q2\n0 1\nq0\nq0 q2\nq0 0 q1\nq0 1 q2\nq1 0 q1\nq1 1 q2\nq2 0 q1\nq2 1 q2'
AN='s0 s1\n0 1\ns0\ns0\ns0 0 s1\ns0 1 s0\ns1 0 s1\ns1 1 s0'
AO='q0 q1 q2\na b\nz0 z1\nq0\nz0\nq0\nq0 a z0 z0z1 q1\nq1 a z1 z1z1 q1\nq1 b z1 E q2\nq2 b z1 E q2\nq2 E z0 E q0'
AP='IGEN\nNEM\nNEM\nNEM\nNEM\nNEM'
AQ='q0 q1 q2 q3\na b\nz0 z1\nq0\nz0\nq3\nq0 a z0 z0z1 q1\nq1 a z1 z1z1 q1\nq1 b z1 E q2\nq2 b z1 E q2\nq2 b z0 z0z0 q2\nq2 E z0 E q0'
AR='IGEN\nIGEN\nNEM\nNEM\nNEM'
u=[{D:'Problem 1 (DFA - Deterministic Finite Automaton)',g:J,h:[{D:'Case 1',H:G.FILE,N:S.TEST_EQUAL,E:q,I:r,U:[i,'10101,111,111110111010101,001,0021']},{D:'Case 2',H:G.FILE,N:S.TEST_EQUAL,E:s,I:t,U:[i,'a,aa,abab,bbb,aaaaaaaaaaaab,aaaaabbbbb,aaaabbbbba,c']}]}]
class C(Exception):0
def c():return A.path.join(R._get_default_tempdir(),next(R._get_candidate_names()))
def v(environment,case):
	B=case;A=environment;C=copy.deepcopy(A[V]);D=B.get(U,[])
	if B[H]==G.FILE:C.extend(['--input',A[E],'--output',A[I]])
	if B[H]==G.CONSOLE:F=B[E]+W;J=X
	else:F=O;J=O
	if D:C.extend(D)
	A[j]=C;A[k]=F;A[l]=J
def w(environment,case):
	A=environment;v(A,case)
	try:
		D=F.run(A[j],cwd=A[Y],capture_output=J,text=J,input=A[k],encoding=A[l])
		for E in[D.stdout,D.stderr]:
			if E:
				E=E.strip()
				if E:B(E.strip())
		if D.returncode!=0:raise C(f"Program exited with status code {D.returncode}")
		A[m]=D.stdout.strip()
	except F.CalledProcessError as G:raise C(f"Couldn't run project: {G}")
def x(folder):
	for(B,G,C)in A.walk(folder):
		for D in C:
			if D=='__main__.py':E=A.path.dirname(B);F=A.path.basename(B);return{n:M.PYTHON,K:E,o:F}
def y(folder):
	for(B,E,C)in A.walk(folder):
		for D in C:
			if D=='CMakeLists.txt':return{n:M.CPP,K:B}
def z(folder):
	for(C,G,D)in A.walk(folder):
		for E in D:
			B=A.path.join(C,E)
			try:
				with T(B,'rb')as F:
					if F.read(4)==b'\x7fELF':return B
			except:0
def A0(environment):A=environment;B=A[o];A[Y]=A[K];A[V]=['python3','-m',B]
def A1(environment):
	B=environment;A=R.mkdtemp()
	try:F.run(['cmake','-DCMAKE_BUILD_TYPE=Release',B[K]],cwd=A,check=J)
	except F.CalledProcessError as E:raise C(f"Could not configure CMake project")
	try:F.run(['make','-j',str(p.cpu_count())],cwd=A)
	except F.CalledProcessError as E:raise C(f"Could not build CMake project")
	D=z(A)
	if not D:raise C(f"Couldn't find built executable in CMake project")
	B[Y]=A;B[V]=[D]
def A2(case,environment):
	A=environment;B=c();C=c();A[E]=B;A[I]=C
	with T(B,'w',encoding=X)as D:D.write(case[E])
def A3(case,environment):
	D=environment;F=D[E];B=D[I]
	if not A.path.exists(B):raise C(f"Output file not created by program")
	with T(B,'r',encoding=X)as G:H=G.read().strip()
	if not e[case[N]](case,H):raise C(f"Output mismatch: expected different output in file")
	if A.path.exists(F):A.remove(F)
	if A.path.exists(B):A.remove(B)
def A4(case,environment):
	if not e[case[N]](case,environment[m]):raise C(f"Output mismatch: expected different output on stdout")
def d(text):return W.join([A.strip()for A in text.strip().split(W)])
def A5(case,output):B=d(output);A=case[I];C=[A]if isinstance(A,str)else A;return any([d(A)==B for A in C])
A6={M.PYTHON:{D:'Python',Z:x,a:A0},M.CPP:{D:'CMake (C++)',Z:y,a:A1}}
A7={G.FILE:{P:A2,b:A3},G.CONSOLE:{P:O,b:A4}}
e={S.TEST_EQUAL:A5}
def A8():
	R=A.getcwd();E=O
	for(S,G)in A6.items():
		E=G[Z](R)
		if E:break
	if not E:B("❌ Couldn't find any project in the current folder ❌");L.exit(1)
	B(f"Found {G[D]} project in {E[K]}")
	try:G[a](E)
	except C as I:B(f"❌ Error during build: {I}");L.exit(2)
	B('Running tests...');Q=False
	for M in u:
		if not M[g]:continue
		B(f"Problem: {M[D]}")
		for F in M[h]:
			B(f"Running case: {F[D]}")
			try:
				N=A7[F[H]]
				if N[P]:N[P](F,E)
				w(E,F)
				if F[H]:N[b](F,E)
			except C as I:B(f"❌ Failed {F[D]}: {I} ❌");Q=J;continue
			B(f"🎉 {F[D]} succeeded 🎉")
	if Q:B('❌ Some tests failed. ❌');L.exit(3)
	B('🎉 All tests passed! Congratulations! 🎉');L.exit(0)
if __name__=='__main__':A8()