n='package'
m='language'
l='stdout'
k='encoding'
j='stdin'
i='command'
h='Case 2'
g='--check'
f='Case 1'
c='verify'
b='prepare'
a='find'
Z='cwd'
Y='utf-8'
X='languageCommand'
W='cases'
V=open
S='setup'
R=True
Q=None
P='--det'
M='root'
K='arguments'
I='testType'
H='output'
G='inputType'
D='input'
C=print
A='name'
from enum import Enum as T
import tempfile as U,subprocess as L,multiprocessing as o,copy,sys as N,os as B
class E(T):FILE=0;CONSOLE=1
class J(T):TEST_EQUAL=0
class O(T):PYTHON=0;CPP=1
p='q0 q1 q2\n0 1\nq0\nq0\nq0 0 q2\nq0 1 q1\nq1 0 q2\nq1 1 q0\nq2 0 q1\nq2 1 q2'
q='IGEN\nNEM\nIGEN\nIGEN\nNEM'
r='q0 q1 q2\na b\nq0\nq1 q2\nq0 a q1\nq1 a q1\nq1 b q2\nq2 b q2'
s='IGEN\nIGEN\nNEM\nNEM\nIGEN\nIGEN\nNEM\nNEM'
t='q0 q1 q2\n0 1\nq0\nq2\nq0 0 q1\nq0 0 q2\nq0 1 q1\nq1 0 q2\nq1 1 q2'
u='s0 s1 s2 s3\n0 1\ns0\ns1 s3\ns0 0 s1\ns0 1 s2\ns1 0 s3\ns1 1 s3\ns2 0 s3\ns2 1 s3'
v='q0 q1 q2\n0 1\nq0\nq2\nq0 0 q0\nq0 0 q1\nq0 1 q0\nq0 1 q1\nq1 0 q1\nq1 0 q2\nq1 1 q0\nq1 1 q1\nq1 1 q2\nq2 0 q1'
w='s0 s1 s2\n0 1\ns0\ns2\ns0 0 s1\ns0 1 s1\ns1 0 s2\ns1 1 s2\ns2 0 s2\ns2 1 s2'
x='q0 q1 q2 q3\n0 1\nq0\nq1 q3\nq0 0 q2\nq0 1 q1\nq1 0 q1\nq1 1 q2\nq1 1 q3\nq2 1 q2\nq3 0 q2\nq3 0 q3\nq3 1 q2'
y='s0 s1 s2 s3\n0 1\ns0\ns2 s3\ns0 0 s1\ns0 1 s2\ns1 1 s1\ns2 0 s2\ns2 1 s3\ns3 0 s3\ns3 1 s1'
z='q0 q1\n0 1\nq0\nq1\nq0 0 q0\nq0 1 q1\nq1 0 q0\nq1 1 q1'
A0='s0 s1\n0 1\ns0\ns1\ns0 0 s0\ns0 1 s1\ns1 0 s0\ns1 1 s1'
A1=[{A:'Problem 1 (DFA - Deterministic Finite Automaton)',W:[{A:f,G:E.FILE,I:J.TEST_EQUAL,D:p,H:q,K:[g,'10101,111,111110111010101,001,0021']},{A:h,G:E.FILE,I:J.TEST_EQUAL,D:r,H:s,K:[g,'a,aa,abab,bbb,aaaaaaaaaaaab,aaaaabbbbb,aaaabbbbba,c']}]},{A:'Problem 2 (Transforming a Non-Deterministic Finite Automata Into a Deterministic One)',W:[{A:f,G:E.FILE,I:J.TEST_EQUAL,D:t,H:u,K:[P]},{A:h,G:E.FILE,I:J.TEST_EQUAL,D:v,H:w,K:[P]},{A:'Case 3',G:E.FILE,I:J.TEST_EQUAL,D:x,H:y,K:[P]},{A:'Case 4',G:E.FILE,I:J.TEST_EQUAL,D:z,H:A0,K:[P]}]}]
class F(Exception):0
def d():return B.path.join(U._get_default_tempdir(),next(U._get_candidate_names()))
def A2(environment,case):
	B=case;A=environment;C=copy.deepcopy(A[X]);F=B.get(K,[])
	if B[G]==E.FILE:C.extend(['--input',A[D],'--output',A[H]])
	if B[G]==E.CONSOLE:I=B[D]+'\n';J=Y
	else:I=Q;J=Q
	if F:C.extend(F)
	A[i]=C;A[j]=I;A[k]=J
def A3(environment,case):
	A=environment;A2(A,case)
	try:
		B=L.run(A[i],cwd=A[Z],capture_output=R,text=R,input=A[j],encoding=A[k])
		for D in[B.stdout,B.stderr]:
			if D:
				D=D.strip()
				if D:C(D.strip())
		if B.returncode!=0:raise F(f"Program exited with status code {B.returncode}")
		A[l]=B.stdout.strip()
	except L.CalledProcessError as E:raise F(f"Couldn't run project: {E}")
def A4(folder):
	for(A,G,C)in B.walk(folder):
		for D in C:
			if D=='__main__.py':E=B.path.dirname(A);F=B.path.basename(A);return{m:O.PYTHON,M:E,n:F}
def A5(folder):
	for(A,E,C)in B.walk(folder):
		for D in C:
			if D=='CMakeLists.txt':return{m:O.CPP,M:A}
def A6(folder):
	for(C,G,D)in B.walk(folder):
		for E in D:
			A=B.path.join(C,E)
			try:
				with V(A,'rb')as F:
					if F.read(4)==b'\x7fELF':return A
			except:pass
def A7(environment):A=environment;B=A[n];A[Z]=A[M];A[X]=['python3','-m',B]
def A8(environment):
	B=environment;A=U.mkdtemp()
	try:L.run(['cmake','-DCMAKE_BUILD_TYPE=Release',B[M]],cwd=A,check=R)
	except L.CalledProcessError as D:raise F(f"Could not configure CMake project")
	try:L.run(['make','-j',str(o.cpu_count())],cwd=A)
	except L.CalledProcessError as D:raise F(f"Could not build CMake project")
	C=A6(A)
	if not C:raise F(f"Couldn't find built executable in CMake project")
	B[Z]=A;B[X]=[C]
def A9(case,environment):
	A=environment;B=d();C=d();A[D]=B;A[H]=C
	with V(B,'w',encoding=Y)as E:E.write(case[D])
def AA(case,environment):
	C=environment;E=C[D];A=C[H]
	if not B.path.exists(A):raise F(f"Output file not created by program")
	with V(A,'r',encoding=Y)as G:J=G.read().strip()
	if not e[case[I]](case,J):raise F(f"Output mismatch: expected different output in file")
	if B.path.exists(E):B.remove(E)
	if B.path.exists(A):B.remove(A)
def AB(case,environment):
	if not e[case[I]](case,environment[l]):raise F(f"Output mismatch: expected different output on stdout")
def AC(case,output):return output.strip()==case[H].strip()
AD={O.PYTHON:{A:'Python',a:A4,b:A7},O.CPP:{A:'CMake (C++)',a:A5,b:A8}}
AE={E.FILE:{S:A9,c:AA},E.CONSOLE:{S:Q,c:AB}}
e={J.TEST_EQUAL:AC}
def AF():
	O=B.getcwd();D=Q
	for(P,H)in AD.items():
		D=H[a](O)
		if D:break
	if not D:C("❌ Couldn't find any project in the current folder ❌");N.exit(1)
	C(f"Found {H[A]} project in {D[M]}")
	try:H[b](D)
	except F as I:C(f"❌ Error during build: {I}");N.exit(2)
	C('Running tests...');K=False
	for L in A1:
		C(f"Problem: {L[A]}")
		for E in L[W]:
			C(f"Running case: {E[A]}")
			try:
				J=AE[E[G]]
				if J[S]:J[S](E,D)
				A3(D,E)
				if E[G]:J[c](E,D)
			except F as I:C(f"❌ Failed {E[A]}: {I} ❌");K=R;continue
			C(f"🎉 {E[A]} succeeded 🎉")
	if K:C('❌ Some tests failed. ❌');N.exit(3)
	C('🎉 All tests passed! Congratulations! 🎉');N.exit(0)
if __name__=='__main__':AF()