r='package'
q='language'
p='stdout'
o='encoding'
n='stdin'
m='command'
l='Case 2'
k='--check'
j='Case 1'
i='s0 s1 s2 s3\n0 1\ns0\ns2\ns0 0 s1\ns0 1 s3\ns1 0 s3\ns1 1 s2\ns2 0 s0\ns2 1 s2\ns3 0 s3\ns3 1 s0'
e='verify'
d='prepare'
c='find'
b='cwd'
a='utf-8'
Z='\n'
Y='languageCommand'
X='cases'
W='enabled'
V=open
S='setup'
R=None
Q='--det'
N='root'
M=True
K='arguments'
I='testType'
H='output'
G='inputType'
D='input'
C=print
A='name'
from enum import Enum as T
import tempfile as U,subprocess as L,multiprocessing as s,copy,sys as O,os as B
class E(T):FILE=0;CONSOLE=1
class J(T):TEST_EQUAL=0
class P(T):PYTHON=0;CPP=1
t='q0 q1 q2\n0 1\nq0\nq0\nq0 0 q2\nq0 1 q1\nq1 0 q2\nq1 1 q0\nq2 0 q1\nq2 1 q2'
u='IGEN\nNEM\nIGEN\nIGEN\nNEM'
v='q0 q1 q2\na b\nq0\nq1 q2\nq0 a q1\nq1 a q1\nq1 b q2\nq2 b q2'
w='IGEN\nIGEN\nNEM\nNEM\nIGEN\nIGEN\nNEM\nNEM'
x='q0 q1 q2\n0 1\nq0\nq2\nq0 0 q1\nq0 0 q2\nq0 1 q1\nq1 0 q2\nq1 1 q2'
y='s0 s1 s2 s3\n0 1\ns0\ns1 s3\ns0 0 s1\ns0 1 s2\ns1 0 s3\ns1 1 s3\ns2 0 s3\ns2 1 s3'
z='q0 q1 q2\n0 1\nq0\nq2\nq0 0 q0\nq0 0 q1\nq0 1 q0\nq0 1 q1\nq1 0 q1\nq1 0 q2\nq1 1 q0\nq1 1 q1\nq1 1 q2\nq2 0 q1'
A0='s0 s1 s2\n0 1\ns0\ns2\ns0 0 s1\ns0 1 s1\ns1 0 s2\ns1 1 s2\ns2 0 s2\ns2 1 s2'
A1='q0 q1 q2 q3\n0 1\nq0\nq1 q3\nq0 0 q2\nq0 1 q1\nq1 0 q1\nq1 1 q2\nq1 1 q3\nq2 1 q2\nq3 0 q2\nq3 0 q3\nq3 1 q2'
A2='s0 s1 s2 s3\n0 1\ns0\ns2 s3\ns0 0 s1\ns0 1 s2\ns1 1 s1\ns2 0 s2\ns2 1 s3\ns3 0 s3\ns3 1 s1'
A3='q0 q1\n0 1\nq0\nq1\nq0 0 q0\nq0 1 q1\nq1 0 q0\nq1 1 q1'
A4='s0 s1\n0 1\ns0\ns1\ns0 0 s0\ns0 1 s1\ns1 0 s0\ns1 1 s1'
AK='q0 q1 q2 q3 q4 q5\n0 1\nq0\nq2\nq0 0 q1\nq0 1 q4\nq1 0 q4\nq1 1 q2\nq2 0 q0\nq2 1 q2\nq3 0 q5\nq3 1 q4\nq4 0 q4\nq4 1 q3\nq5 0 q4\nq5 1 q2'
AL='s0 s1 s2 s4\n0 1\ns0\ns2\ns0 0 s1\ns0 1 s4\ns1 0 s4\ns1 1 s2\ns2 0 s0\ns2 1 s2\ns4 0 s4\ns4 1 s0'
AM=i
AN='q0 q1 q2 q3\n0 1\nq0\nq2\nq0 0 q1\nq0 1 q3\nq1 0 q3\nq1 1 q2\nq2 0 q0\nq2 1 q2\nq3 0 q3\nq3 1 q0'
AO=i
AP='q0 q1 q2\n0 1\nq0\nq0 q2\nq0 0 q1\nq0 1 q2\nq1 0 q1\nq1 1 q2\nq2 0 q1\nq2 1 q2'
AQ='s0 s1\n0 1\ns0\ns0\ns0 0 s1\ns0 1 s0\ns1 0 s1\ns1 1 s0'
AR='q0 q1 q2\na b\nz0 z1\nq0\nz0\nq0\nq0 a z0 z0z1 q1\nq1 a z1 z1z1 q1\nq1 b z1 E q2\nq2 b z1 E q2\nq2 E z0 E q0'
AS='IGEN\nNEM\nNEM\nNEM\nNEM\nNEM'
AT='q0 q1 q2 q3\na b\nz0 z1\nq0\nz0\nq3\nq0 a z0 z0z1 q1\nq1 a z1 z1z1 q1\nq1 b z1 E q2\nq2 b z1 E q2\nq2 b z0 z0z0 q2\nq2 E z0 E q0'
AU='IGEN\nIGEN\nNEM\nNEM\nNEM'
A5=[{A:'Problem 1 (DFA - Deterministic Finite Automaton)',W:M,X:[{A:j,G:E.FILE,I:J.TEST_EQUAL,D:t,H:u,K:[k,'10101,111,111110111010101,001,0021']},{A:l,G:E.FILE,I:J.TEST_EQUAL,D:v,H:w,K:[k,'a,aa,abab,bbb,aaaaaaaaaaaab,aaaaabbbbb,aaaabbbbba,c']}]},{A:'Problem 2 (Transforming a Non-Deterministic Finite Automata Into a Deterministic One)',W:M,X:[{A:j,G:E.FILE,I:J.TEST_EQUAL,D:x,H:y,K:[Q]},{A:l,G:E.FILE,I:J.TEST_EQUAL,D:z,H:A0,K:[Q]},{A:'Case 3',G:E.FILE,I:J.TEST_EQUAL,D:A1,H:A2,K:[Q]},{A:'Case 4',G:E.FILE,I:J.TEST_EQUAL,D:A3,H:A4,K:[Q]}]}]
class F(Exception):0
def f():return B.path.join(U._get_default_tempdir(),next(U._get_candidate_names()))
def A6(environment,case):
	B=case;A=environment;C=copy.deepcopy(A[Y]);F=B.get(K,[])
	if B[G]==E.FILE:C.extend(['--input',A[D],'--output',A[H]])
	if B[G]==E.CONSOLE:I=B[D]+Z;J=a
	else:I=R;J=R
	if F:C.extend(F)
	A[m]=C;A[n]=I;A[o]=J
def A7(environment,case):
	A=environment;A6(A,case)
	try:
		B=L.run(A[m],cwd=A[b],capture_output=M,text=M,input=A[n],encoding=A[o])
		for D in[B.stdout,B.stderr]:
			if D:
				D=D.strip()
				if D:C(D.strip())
		if B.returncode!=0:raise F(f"Program exited with status code {B.returncode}")
		A[p]=B.stdout.strip()
	except L.CalledProcessError as E:raise F(f"Couldn't run project: {E}")
def A8(folder):
	for(A,G,C)in B.walk(folder):
		for D in C:
			if D=='__main__.py':E=B.path.dirname(A);F=B.path.basename(A);return{q:P.PYTHON,N:E,r:F}
def A9(folder):
	for(A,E,C)in B.walk(folder):
		for D in C:
			if D=='CMakeLists.txt':return{q:P.CPP,N:A}
def AA(folder):
	for(C,G,D)in B.walk(folder):
		for E in D:
			A=B.path.join(C,E)
			try:
				with V(A,'rb')as F:
					if F.read(4)==b'\x7fELF':return A
			except:0
def AB(environment):A=environment;B=A[r];A[b]=A[N];A[Y]=['python3','-m',B]
def AC(environment):
	B=environment;A=U.mkdtemp()
	try:L.run(['cmake','-DCMAKE_BUILD_TYPE=Release',B[N]],cwd=A,check=M)
	except L.CalledProcessError as D:raise F(f"Could not configure CMake project")
	try:L.run(['make','-j',str(s.cpu_count())],cwd=A)
	except L.CalledProcessError as D:raise F(f"Could not build CMake project")
	C=AA(A)
	if not C:raise F(f"Couldn't find built executable in CMake project")
	B[b]=A;B[Y]=[C]
def AD(case,environment):
	A=environment;B=f();C=f();A[D]=B;A[H]=C
	with V(B,'w',encoding=a)as E:E.write(case[D])
def AE(case,environment):
	C=environment;E=C[D];A=C[H]
	if not B.path.exists(A):raise F(f"Output file not created by program")
	with V(A,'r',encoding=a)as G:J=G.read().strip()
	if not h[case[I]](case,J):raise F(f"Output mismatch: expected different output in file")
	if B.path.exists(E):B.remove(E)
	if B.path.exists(A):B.remove(A)
def AF(case,environment):
	if not h[case[I]](case,environment[p]):raise F(f"Output mismatch: expected different output on stdout")
def g(text):return Z.join([A.strip()for A in text.strip().split(Z)])
def AG(case,output):B=g(output);A=case[H];C=[A]if isinstance(A,str)else A;return any([g(A)==B for A in C])
AH={P.PYTHON:{A:'Python',c:A8,d:AB},P.CPP:{A:'CMake (C++)',c:A9,d:AC}}
AI={E.FILE:{S:AD,e:AE},E.CONSOLE:{S:R,e:AF}}
h={J.TEST_EQUAL:AG}
def AJ():
	P=B.getcwd();D=R
	for(Q,H)in AH.items():
		D=H[c](P)
		if D:break
	if not D:C("❌ Couldn't find any project in the current folder ❌");O.exit(1)
	C(f"Found {H[A]} project in {D[N]}")
	try:H[d](D)
	except F as I:C(f"❌ Error during build: {I}");O.exit(2)
	C('Running tests...');L=False
	for J in A5:
		if not J[W]:continue
		C(f"Problem: {J[A]}")
		for E in J[X]:
			C(f"Running case: {E[A]}")
			try:
				K=AI[E[G]]
				if K[S]:K[S](E,D)
				A7(D,E)
				if E[G]:K[e](E,D)
			except F as I:C(f"❌ Failed {E[A]}: {I} ❌");L=M;continue
			C(f"🎉 {E[A]} succeeded 🎉")
	if L:C('❌ Some tests failed. ❌');O.exit(3)
	C('🎉 All tests passed! Congratulations! 🎉');O.exit(0)
if __name__=='__main__':AJ()