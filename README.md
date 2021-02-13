# SiguriaNeInternet-Projekti3

Secili prej nesh e dijmë rëndësinë e kopjimit të fajllit ose lëvizjes së fajllit nga një vend specifik në një tjetër. Në këtë postim, ne jemi përpjekur të shpjegojmë jo vetëm programin, por kemi shtuar disa pjesë interesante të Interface.Ne gjatë ketij projekti do të përdorim "Tkinter" dhe "shutil" për këtë projekt. 

Modulet të cilat kërkohen:

1.shutil - është një modul i python i cili na mundëson që operojmë me lehtësisht me fajllat.Kjo kujdeset per semantiken sikurse krijimi i obejkteve te fajllave, mbylljen e fajllave pasi të kopjohen dhe na lejon të përqendrohemi në logjikën e programit tonë.Ky modul i python është i parainstaluar pra është vendas në librarinë e python dhe nuk kemi nevojë ta insakojmë , perveq që mund ta importojmë kur deshirojmë ta perdorim atë.

2.tkinter - është një lidhje e Python me paketen Tk GUI toolkit.Tkinter përdoret si Graphical User Interface ose Nderfaqe Grafike e përdoruesit për python.Tkinter është gjithashtu biblotek vendase në python , dhe nuk kemi nevojë për ndonjë instalimi të vegles , thjesht para se të përdoret ajo duhet te importohet.

Mënyra e ekzekutimit të kodit:

Pasi kemi bërë run kodin atëherë na hapet GUI(Graphical User Interface) për kodin që ekzekutohet, e cila është krijuar me anë të modulit tkinter.Pas kësaj, shfaqet një label për File i cili do të kopjohet , duke pas mundesinë me zgjedh fajllin e caktuar përmes butonit BROWSE.Ndërsa label tjetër është për të bërë zhvendosjen e fajllit nga lokacioni aktual deri në lokacionin tjetër.

Gjatë programit janë caktuar poashtu edhe burimi nga vjen fajlli dhe destinacioni në të cilen ai fajll do të zhvendoset.Për këtë janë përdorur funksionet:

SourceBrowse()

DestinationBrowse()

CopyFile()

MoveFile()

Poashtu është përdorur edhe disa messagebox në rastet kur operacioni i COPY ose MOVE nuk arrihet të ekzekutohet për një qëllim të caktuar.
Poshtë kemi edhe dy butona tjerë COPY FILE DHE MOVE FILE.Butoni i parë pasi të mbushen te dy label , mundëson kopjimin e fajllit nga një folder në folderin tjetër , duke pas mundesinë që ai fajll i caktuar, të jetë i pranishem edhe në folderin e mëparshem edhe në folderin e ri.Ndërsa butoni i dytë MOVE FILE sillet sikur komanda "CUT" , pra e zhvendos fajllin nga folderi 1 në folderin 2 , dhe ne folderin 1 pas këtij operacioni ai fajll nuk ndodhet më.Gjatë kësaj detyre janë përdorur disa funksione të ndryshme të cilat na kanë lehtësuar punën gjatë detyrës.
