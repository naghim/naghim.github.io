u='package'
t='language'
s='stdout'
r='encoding'
q='stdin'
p='command'
o=False
n='Case 3'
m='--check'
l='s0 s1 s2 s3\n0 1\ns0\ns2\ns0 0 s1\ns0 1 s3\ns1 0 s3\ns1 1 s2\ns2 0 s0\ns2 1 s2\ns3 0 s3\ns3 1 s0'
h='verify'
g='prepare'
f='find'
e='cwd'
d='utf-8'
c='\n'
b='languageCommand'
a='--mini'
Z='Case 2'
Y='Case 1'
X=open
U='setup'
T=None
S='--det'
R='cases'
Q='enabled'
N='root'
M=True
K='arguments'
H='testType'
G=print
F='output'
E='inputType'
B='input'
A='name'
from enum import Enum as V
import tempfile as W,subprocess as L,multiprocessing as v,copy,sys as O,os as C
class D(V):FILE=0;CONSOLE=1
class I(V):TEST_EQUAL=0
class P(V):PYTHON=0;CPP=1
w='q0 q1 q2\n0 1\nq0\nq0\nq0 0 q2\nq0 1 q1\nq1 0 q2\nq1 1 q0\nq2 0 q1\nq2 1 q2'
x='IGEN\nNEM\nIGEN\nIGEN\nNEM'
y='q0 q1 q2\na b\nq0\nq1 q2\nq0 a q1\nq1 a q1\nq1 b q2\nq2 b q2'
z='IGEN\nIGEN\nNEM\nNEM\nIGEN\nIGEN\nNEM\nNEM'
A0='q0 q1 q2\n0 1\nq0\nq2\nq0 0 q1\nq0 0 q2\nq0 1 q1\nq1 0 q2\nq1 1 q2'
A1='s0 s1 s2 s3\n0 1\ns0\ns1 s3\ns0 0 s1\ns0 1 s2\ns1 0 s3\ns1 1 s3\ns2 0 s3\ns2 1 s3'
A2='q0 q1 q2\n0 1\nq0\nq2\nq0 0 q0\nq0 0 q1\nq0 1 q0\nq0 1 q1\nq1 0 q1\nq1 0 q2\nq1 1 q0\nq1 1 q1\nq1 1 q2\nq2 0 q1'
A3='s0 s1 s2\n0 1\ns0\ns2\ns0 0 s1\ns0 1 s1\ns1 0 s2\ns1 1 s2\ns2 0 s2\ns2 1 s2'
A4='q0 q1 q2 q3\n0 1\nq0\nq1 q3\nq0 0 q2\nq0 1 q1\nq1 0 q1\nq1 1 q2\nq1 1 q3\nq2 1 q2\nq3 0 q2\nq3 0 q3\nq3 1 q2'
A5='s0 s1 s2 s3\n0 1\ns0\ns2 s3\ns0 0 s1\ns0 1 s2\ns1 1 s1\ns2 0 s2\ns2 1 s3\ns3 0 s3\ns3 1 s1'
A6='q0 q1\n0 1\nq0\nq1\nq0 0 q0\nq0 1 q1\nq1 0 q0\nq1 1 q1'
A7='s0 s1\n0 1\ns0\ns1\ns0 0 s0\ns0 1 s1\ns1 0 s0\ns1 1 s1'
A8='q0 q1 q2 q3 q4 q5\n0 1\nq0\nq2\nq0 0 q1\nq0 1 q4\nq1 0 q4\nq1 1 q2\nq2 0 q0\nq2 1 q2\nq3 0 q5\nq3 1 q4\nq4 0 q4\nq4 1 q3\nq5 0 q4\nq5 1 q2'
A9='s0 s1 s2 s4\n0 1\ns0\ns2\ns0 0 s1\ns0 1 s4\ns1 0 s4\ns1 1 s2\ns2 0 s0\ns2 1 s2\ns4 0 s4\ns4 1 s0'
AA=l
AB='q0 q1 q2 q3\n0 1\nq0\nq2\nq0 0 q1\nq0 1 q3\nq1 0 q3\nq1 1 q2\nq2 0 q0\nq2 1 q2\nq3 0 q3\nq3 1 q0'
AC=l
AD='q0 q1 q2\n0 1\nq0\nq0 q2\nq0 0 q1\nq0 1 q2\nq1 0 q1\nq1 1 q2\nq2 0 q1\nq2 1 q2'
AE='s0 s1\n0 1\ns0\ns0\ns0 0 s1\ns0 1 s0\ns1 0 s1\ns1 1 s0'
AU='q0 q1 q2\na b\nz0 z1\nq0\nz0\nq0\nq0 a z0 z0z1 q1\nq1 a z1 z1z1 q1\nq1 b z1 E q2\nq2 b z1 E q2\nq2 E z0 E q0'
AV='IGEN\nNEM\nNEM\nNEM\nNEM\nNEM'
AW='q0 q1 q2 q3\na b\nz0 z1\nq0\nz0\nq3\nq0 a z0 z0z1 q1\nq1 a z1 z1z1 q1\nq1 b z1 E q2\nq2 b z1 E q2\nq2 b z0 z0z0 q2\nq2 E z0 E q0'
AX='IGEN\nIGEN\nNEM\nNEM\nNEM'
AF=[{A:'Problem 1 (DFA - Deterministic Finite Automaton)',Q:M,R:[{A:Y,E:D.FILE,H:I.TEST_EQUAL,B:w,F:x,K:[m,'10101,111,111110111010101,001,0021']},{A:Z,E:D.FILE,H:I.TEST_EQUAL,B:y,F:z,K:[m,'a,aa,abab,bbb,aaaaaaaaaaaab,aaaaabbbbb,aaaabbbbba,c']}]},{A:'Problem 2 (Transforming a Non-Deterministic Finite Automata Into a Deterministic One)',Q:M,R:[{A:Y,E:D.FILE,H:I.TEST_EQUAL,B:A0,F:A1,K:[S]},{A:Z,E:D.FILE,H:I.TEST_EQUAL,B:A2,F:A3,K:[S]},{A:n,E:D.FILE,H:I.TEST_EQUAL,B:A4,F:A5,K:[S]},{A:'Case 4',E:D.FILE,H:I.TEST_EQUAL,B:A6,F:A7,K:[S]}]},{A:'Problem 3 (Minimizing a Finite Automaton)',Q:o,R:[{A:Y,E:D.FILE,H:I.TEST_EQUAL,B:A8,F:[A9,AA],K:[a]},{A:Z,E:D.FILE,H:I.TEST_EQUAL,B:AB,F:AC,K:[a]},{A:n,E:D.FILE,H:I.TEST_EQUAL,B:AD,F:AE,K:[a]}]}]
class J(Exception):0
def i():return C.path.join(W._get_default_tempdir(),next(W._get_candidate_names()))
def AG(environment,case):
	C=case;A=environment;G=copy.deepcopy(A[b]);H=C.get(K,[])
	if C[E]==D.FILE:G.extend(['--input',A[B],'--output',A[F]])
	if C[E]==D.CONSOLE:I=C[B]+c;J=d
	else:I=T;J=T
	if H:G.extend(H)
	A[p]=G;A[q]=I;A[r]=J
def AH(environment,case):
	A=environment;AG(A,case)
	try:
		B=L.run(A[p],cwd=A[e],capture_output=M,text=M,input=A[q],encoding=A[r])
		for C in[B.stdout,B.stderr]:
			if C:
				C=C.strip()
				if C:G(C.strip())
		if B.returncode!=0:raise J(f"Program exited with status code {B.returncode}")
		A[s]=B.stdout.strip()
	except L.CalledProcessError as D:raise J(f"Couldn't run project: {D}")
def AI(folder):
	for(A,G,B)in C.walk(folder):
		for D in B:
			if D=='__main__.py':E=C.path.dirname(A);F=C.path.basename(A);return{t:P.PYTHON,N:E,u:F}
def AJ(folder):
	for(A,E,B)in C.walk(folder):
		for D in B:
			if D=='CMakeLists.txt':return{t:P.CPP,N:A}
def AK(folder):
	for(B,G,D)in C.walk(folder):
		for E in D:
			A=C.path.join(B,E)
			try:
				with X(A,'rb')as F:
					if F.read(4)==b'\x7fELF':return A
			except:0
def AL(environment):A=environment;B=A[u];A[e]=A[N];A[b]=['python3','-m',B]
def AM(environment):
	B=environment;A=W.mkdtemp()
	try:L.run(['cmake','-DCMAKE_BUILD_TYPE=Release',B[N]],cwd=A,check=M)
	except L.CalledProcessError as D:raise J(f"Could not configure CMake project")
	try:L.run(['make','-j',str(v.cpu_count())],cwd=A)
	except L.CalledProcessError as D:raise J(f"Could not build CMake project")
	C=AK(A)
	if not C:raise J(f"Couldn't find built executable in CMake project")
	B[e]=A;B[b]=[C]
def AN(case,environment):
	A=environment;C=i();D=i();A[B]=C;A[F]=D
	with X(C,'w',encoding=d)as E:E.write(case[B])
def AO(case,environment):
	D=environment;E=D[B];A=D[F]
	if not C.path.exists(A):raise J(f"Output file not created by program")
	with X(A,'r',encoding=d)as G:I=G.read().strip()
	if not k[case[H]](case,I):raise J(f"Output mismatch: expected different output in file")
	if C.path.exists(E):C.remove(E)
	if C.path.exists(A):C.remove(A)
def AP(case,environment):
	if not k[case[H]](case,environment[s]):raise J(f"Output mismatch: expected different output on stdout")
def j(text):return c.join([A.strip()for A in text.strip().split(c)])
def AQ(case,output):B=j(output);A=case[F];C=[A]if isinstance(A,str)else A;return any([j(A)==B for A in C])
AR={P.PYTHON:{A:'Python',f:AI,g:AL},P.CPP:{A:'CMake (C++)',f:AJ,g:AM}}
AS={D.FILE:{U:AN,h:AO},D.CONSOLE:{U:T,h:AP}}
k={I.TEST_EQUAL:AQ}
def AT():
	P=C.getcwd();B=T
	for(S,F)in AR.items():
		B=F[f](P)
		if B:break
	if not B:G("❌ Couldn't find any project in the current folder ❌");O.exit(1)
	G(f"Found {F[A]} project in {B[N]}")
	try:F[g](B)
	except J as H:G(f"❌ Error during build: {H}");O.exit(2)
	G('Running tests...');L=o
	for I in AF:
		if not I[Q]:continue
		G(f"Problem: {I[A]}")
		for D in I[R]:
			G(f"Running case: {D[A]}")
			try:
				K=AS[D[E]]
				if K[U]:K[U](D,B)
				AH(B,D)
				if D[E]:K[h](D,B)
			except J as H:G(f"❌ Failed {D[A]}: {H} ❌");L=M;continue
			G(f"🎉 {D[A]} succeeded 🎉")
	if L:G('❌ Some tests failed. ❌');O.exit(3)
	G('🎉 All tests passed! Congratulations! 🎉');O.exit(0)
if __name__=='__main__':AT()
