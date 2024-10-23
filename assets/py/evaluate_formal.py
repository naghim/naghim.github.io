p='package'
o='language'
n='stdout'
m='encoding'
l='stdin'
k='command'
j='Case 3'
i='--check'
f='verify'
e='prepare'
d='find'
c='cwd'
b='utf-8'
a='languageCommand'
Z='--mini'
Y='Case 2'
X='Case 1'
W=open
T='setup'
S=True
R=None
Q='--det'
P='cases'
M='root'
K='arguments'
H='testType'
G=print
F='output'
E='inputType'
B='input'
A='name'
from enum import Enum as U
import tempfile as V,subprocess as L,multiprocessing as q,copy,sys as N,os as C
class D(U):FILE=0;CONSOLE=1
class I(U):TEST_EQUAL=0
class O(U):PYTHON=0;CPP=1
r='q0 q1 q2\n0 1\nq0\nq0\nq0 0 q2\nq0 1 q1\nq1 0 q2\nq1 1 q0\nq2 0 q1\nq2 1 q2'
s='IGEN\nNEM\nIGEN\nIGEN\nNEM'
t='q0 q1 q2\na b\nq0\nq1 q2\nq0 a q1\nq1 a q1\nq1 b q2\nq2 b q2'
u='IGEN\nIGEN\nNEM\nNEM\nIGEN\nIGEN\nNEM\nNEM'
v='q0 q1 q2\n0 1\nq0\nq2\nq0 0 q1\nq0 0 q2\nq0 1 q1\nq1 0 q2\nq1 1 q2'
w='s0 s1 s2 s3\n0 1\ns0\ns1 s3\ns0 0 s1\ns0 1 s2\ns1 0 s3\ns1 1 s3\ns2 0 s3\ns2 1 s3'
x='q0 q1 q2\n0 1\nq0\nq2\nq0 0 q0\nq0 0 q1\nq0 1 q0\nq0 1 q1\nq1 0 q1\nq1 0 q2\nq1 1 q0\nq1 1 q1\nq1 1 q2\nq2 0 q1'
y='s0 s1 s2\n0 1\ns0\ns2\ns0 0 s1\ns0 1 s1\ns1 0 s2\ns1 1 s2\ns2 0 s2\ns2 1 s2'
z='q0 q1 q2 q3\n0 1\nq0\nq1 q3\nq0 0 q2\nq0 1 q1\nq1 0 q1\nq1 1 q2\nq1 1 q3\nq2 1 q2\nq3 0 q2\nq3 0 q3\nq3 1 q2'
A0='s0 s1 s2 s3\n0 1\ns0\ns2 s3\ns0 0 s1\ns0 1 s2\ns1 1 s1\ns2 0 s2\ns2 1 s3\ns3 0 s3\ns3 1 s1'
A1='q0 q1\n0 1\nq0\nq1\nq0 0 q0\nq0 1 q1\nq1 0 q0\nq1 1 q1'
A2='s0 s1\n0 1\ns0\ns1\ns0 0 s0\ns0 1 s1\ns1 0 s0\ns1 1 s1'
A3='q0 q1 q2 q3 q4 q5\n0 1\nq0\nq2\nq0 0 q1\nq0 1 q4\nq1 0 q4\nq1 1 q2\nq2 0 q0\nq2 1 q2\nq3 0 q5\nq3 1 q4\nq4 0 q4\nq4 1 q3\nq5 0 q4\nq5 1 q2'
A4='s0 s1 s2 s4\n0 1\ns0\ns2\ns0 0 s1\ns0 1 s4\ns1 0 s4\ns1 1 s2\ns2 0 s0\ns2 1 s2\ns4 0 s4\ns4 1 s0'
A5='q0 q1 q2 q3\n0 1\nq0\nq2\nq0 0 q1\nq0 1 q3\nq1 0 q3\nq1 1 q2\nq2 0 q0\nq2 1 q2\nq3 0 q3\nq3 1 q0'
A6='s0 s1 s2 s3\n0 1\ns0\ns2\ns0 0 s1\ns0 1 s3\ns1 0 s3\ns1 1 s2\ns2 0 s0\ns2 1 s2\ns3 0 s3\ns3 1 s0'
A7='q0 q1 q2\n0 1\nq0\nq0 q2\nq0 0 q1\nq0 1 q2\nq1 0 q1\nq1 1 q2\nq2 0 q1\nq2 1 q2'
A8='s0 s1\n0 1\ns0\ns0\ns0 0 s1\ns0 1 s0\ns1 0 s1\ns1 1 s0'
A9=[{A:'Problem 1 (DFA - Deterministic Finite Automaton)',P:[{A:X,E:D.FILE,H:I.TEST_EQUAL,B:r,F:s,K:[i,'10101,111,111110111010101,001,0021']},{A:Y,E:D.FILE,H:I.TEST_EQUAL,B:t,F:u,K:[i,'a,aa,abab,bbb,aaaaaaaaaaaab,aaaaabbbbb,aaaabbbbba,c']}]},{A:'Problem 2 (Transforming a Non-Deterministic Finite Automata Into a Deterministic One)',P:[{A:X,E:D.FILE,H:I.TEST_EQUAL,B:v,F:w,K:[Q]},{A:Y,E:D.FILE,H:I.TEST_EQUAL,B:x,F:y,K:[Q]},{A:j,E:D.FILE,H:I.TEST_EQUAL,B:z,F:A0,K:[Q]},{A:'Case 4',E:D.FILE,H:I.TEST_EQUAL,B:A1,F:A2,K:[Q]}]},{A:'Problem 3 (Minimizing a Finite Automaton)',P:[{A:X,E:D.FILE,H:I.TEST_EQUAL,B:A3,F:A4,K:[Z]},{A:Y,E:D.FILE,H:I.TEST_EQUAL,B:A5,F:A6,K:[Z]},{A:j,E:D.FILE,H:I.TEST_EQUAL,B:A7,F:A8,K:[Z]}]}]
class J(Exception):0
def g():return C.path.join(V._get_default_tempdir(),next(V._get_candidate_names()))
def AA(environment,case):
	C=case;A=environment;G=copy.deepcopy(A[a]);H=C.get(K,[])
	if C[E]==D.FILE:G.extend(['--input',A[B],'--output',A[F]])
	if C[E]==D.CONSOLE:I=C[B]+'\n';J=b
	else:I=R;J=R
	if H:G.extend(H)
	A[k]=G;A[l]=I;A[m]=J
def AB(environment,case):
	A=environment;AA(A,case)
	try:
		B=L.run(A[k],cwd=A[c],capture_output=S,text=S,input=A[l],encoding=A[m])
		for C in[B.stdout,B.stderr]:
			if C:
				C=C.strip()
				if C:G(C.strip())
		if B.returncode!=0:raise J(f"Program exited with status code {B.returncode}")
		A[n]=B.stdout.strip()
	except L.CalledProcessError as D:raise J(f"Couldn't run project: {D}")
def AC(folder):
	for(A,G,B)in C.walk(folder):
		for D in B:
			if D=='__main__.py':E=C.path.dirname(A);F=C.path.basename(A);return{o:O.PYTHON,M:E,p:F}
def AD(folder):
	for(A,E,B)in C.walk(folder):
		for D in B:
			if D=='CMakeLists.txt':return{o:O.CPP,M:A}
def AE(folder):
	for(B,G,D)in C.walk(folder):
		for E in D:
			A=C.path.join(B,E)
			try:
				with W(A,'rb')as F:
					if F.read(4)==b'\x7fELF':return A
			except:pass
def AF(environment):A=environment;B=A[p];A[c]=A[M];A[a]=['python3','-m',B]
def AG(environment):
	B=environment;A=V.mkdtemp()
	try:L.run(['cmake','-DCMAKE_BUILD_TYPE=Release',B[M]],cwd=A,check=S)
	except L.CalledProcessError as D:raise J(f"Could not configure CMake project")
	try:L.run(['make','-j',str(q.cpu_count())],cwd=A)
	except L.CalledProcessError as D:raise J(f"Could not build CMake project")
	C=AE(A)
	if not C:raise J(f"Couldn't find built executable in CMake project")
	B[c]=A;B[a]=[C]
def AH(case,environment):
	A=environment;C=g();D=g();A[B]=C;A[F]=D
	with W(C,'w',encoding=b)as E:E.write(case[B])
def AI(case,environment):
	D=environment;E=D[B];A=D[F]
	if not C.path.exists(A):raise J(f"Output file not created by program")
	with W(A,'r',encoding=b)as G:I=G.read().strip()
	if not h[case[H]](case,I):raise J(f"Output mismatch: expected different output in file")
	if C.path.exists(E):C.remove(E)
	if C.path.exists(A):C.remove(A)
def AJ(case,environment):
	if not h[case[H]](case,environment[n]):raise J(f"Output mismatch: expected different output on stdout")
def AK(case,output):return output.strip()==case[F].strip()
AL={O.PYTHON:{A:'Python',d:AC,e:AF},O.CPP:{A:'CMake (C++)',d:AD,e:AG}}
AM={D.FILE:{T:AH,f:AI},D.CONSOLE:{T:R,f:AJ}}
h={I.TEST_EQUAL:AK}
def AN():
	O=C.getcwd();B=R
	for(Q,F)in AL.items():
		B=F[d](O)
		if B:break
	if not B:G("❌ Couldn't find any project in the current folder ❌");N.exit(1)
	G(f"Found {F[A]} project in {B[M]}")
	try:F[e](B)
	except J as H:G(f"❌ Error during build: {H}");N.exit(2)
	G('Running tests...');K=False
	for L in A9:
		G(f"Problem: {L[A]}")
		for D in L[P]:
			G(f"Running case: {D[A]}")
			try:
				I=AM[D[E]]
				if I[T]:I[T](D,B)
				AB(B,D)
				if D[E]:I[f](D,B)
			except J as H:G(f"❌ Failed {D[A]}: {H} ❌");K=S;continue
			G(f"🎉 {D[A]} succeeded 🎉")
	if K:G('❌ Some tests failed. ❌');N.exit(3)
	G('🎉 All tests passed! Congratulations! 🎉');N.exit(0)
if __name__=='__main__':AN()