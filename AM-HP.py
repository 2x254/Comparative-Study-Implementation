from __future__ import division
import networkx as nx
from networkx.algorithms.community.quality import modularity
import time
import networkx as nx1
import networkx 
from networkx.algorithms.components.connected import connected_components




def transfrom_list_of_sets_to_list_of_lists(list_comm):
    biglist=[list(e) for e in list_comm]
    return biglist

def get_communities_from_txt(path):
    file1 = open(path, 'r')
    Lines = file1.readlines()
    comms=[line.split() for line in Lines]
    file1.close()
    return comms
def tansform_comm_labsl_str(comm):
    l1=[]
    for e in comm:
        subl1=[]
        for el in e:
            subl1.append(str(el))
        l1.append(subl1)
    return l1
        
def tansform_comm_labsl_int(comm):
    l1=[]
    for e in comm:
        subl1=[]
        for el in e:
            subl1.append(int(el))
        l1.append(subl1)
    return l1            
        
    
print("reading data....") 
# synthetic networks LFR_benchmark :   min_comm=50 average_density=5 taux1=3 taux2=1.5
# 1000 nodes and mu between 0.1 and 0.9
#Data = open( 'datasets/LFR/LFR_N1000_ad5_mc50_mu0.1.csv', "r")

#Data = open( 'datasets/LFR/LFR_N1000_ad5_mc50_mu0.2.csv', "r")

#Data = open( 'datasets/LFR/LFR_N1000_ad5_mc50_mu0.3.csv', "r")

#Data = open( 'datasets/LFR/LFR_N1000_ad5_mc50_mu0.4.csv', "r")

#Data = open( 'datasets/LFR/LFR_N1000_ad5_mc50_mu0.5.csv', "r")

#Data = open( 'datasets/LFR/LFR_N1000_ad5_mc50_mu0.6.csv', "r")

#Data = open( 'datasets/LFR/LFR_N1000_ad5_mc50_mu0.7.csv', "r")

#Data = open( 'datasets/LFR/LFR_N1000_ad5_mc50_mu0.8.csv', "r")

#Data = open( 'datasets/LFR/LFR_N1000_ad5_mc50_mu0.9.csv', "r")

# 5000 nodes and mu between 0.1 and 0.9
#Data = open( 'datasets/LFR/LFR_N5000_ad5_mc50_mu0.1.csv', "r")

#Data = open( 'datasets/LFR/LFR_N5000_ad5_mc50_mu0.2.csv', "r")

#Data = open( 'datasets/LFR/LFR_N5000_ad5_mc50_mu0.3.csv', "r")

#Data = open( 'datasets/LFR/LFR_N5000_ad5_mc50_mu0.4.csv', "r")

#Data = open( 'datasets/LFR/LFR_N5000_ad5_mc50_mu0.5.csv', "r")

#Data = open( 'datasets/LFR/LFR_N5000_ad5_mc50_mu0.6.csv', "r")

#Data = open( 'datasets/LFR/LFR_N5000_ad5_mc50_mu0.7.csv', "r")

#Data = open( 'datasets/LFR/LFR_N5000_ad5_mc50_mu0.8.csv', "r")

#Data = open( 'datasets/LFR/LFR_N5000_ad5_mc50_mu0.9.csv', "r")


# 10000 nodes and mu between 0.1 and 0.9
#Data = open( 'datasets/LFR/LFR_N10000_ad5_mc50_mu0.1.csv', "r")

#Data = open( 'datasets/LFR/LFR_N10000_ad5_mc50_mu0.2.csv', "r")

#Data = open( 'datasets/LFR/LFR_N10000_ad5_mc50_mu0.3.csv', "r")

#Data = open( 'datasets/LFR/LFR_N10000_ad5_mc50_mu0.4.csv', "r")

#Data = open( 'datasets/LFR/LFR_N10000_ad5_mc50_mu0.5.csv', "r")

#Data = open( 'datasets/LFR/LFR_N10000_ad5_mc50_mu0.6.csv', "r")

#Data = open( 'datasets/LFR/LFR_N10000_ad5_mc50_mu0.7.csv', "r")

#Data = open( 'datasets/LFR/LFR_N10000_ad5_mc50_mu0.8.csv', "r")

#Data = open( 'datasets/LFR/LFR_N10000_ad5_mc50_mu0.9.csv', "r")

# 50000 nodes and mu between 0.1 and 0.9
#Data = open( 'datasets/LFR/LFR_N50000_ad5_mc50_mu0.1.csv', "r")

#Data = open( 'datasets/LFR/LFR_N50000_ad5_mc50_mu0.2.csv', "r")

#Data = open( 'datasets/LFR/LFR_N50000_ad5_mc50_mu0.3.csv', "r")

#Data = open( 'datasets/LFR/LFR_N50000_ad5_mc50_mu0.4.csv', "r")

#Data = open( 'datasets/LFR/LFR_N50000_ad5_mc50_mu0.5.csv', "r")

#Data = open( 'datasets/LFR/LFR_N50000_ad5_mc50_mu0.6.csv', "r")

#Data = open( 'datasets/LFR/LFR_N50000_ad5_mc50_mu0.7.csv', "r")

#Data = open( 'datasets/LFR/LFR_N50000_ad5_mc50_mu0.8.csv', "r")

#Data = open( 'datasets/LFR/LFR_N50000_ad5_mc50_mu0.9.csv', "r")


print("getting data...")
#real data sets 

#Data=open( "datasets/amazon/Amazon.csv","r")


Data = open( "datasets/karate/karate.csv","r")


#Data = open( "datasets/emailEuCore/emailEucore.csv","r")


#Data = open( "datasets/dolphins/dolphins.csv","r")


#Data = open( "datasets/Books/Books.csv","r")


#Data = open("datasets/cora/cora.csv","r")


#Data = open("datasets/citeseer/citeseer.csv","r")


#Data = open("datasets/youtube/youtube.csv","r")


print("data readed... !")


G = nx.parse_edgelist(Data,nodetype=int)


# (1) calculate similarity

print("calculating similarities...\n")
for (u,v) in G.edges():
    adjU=set(list(G.neighbors(u))).union({u})
    adjV=set(list(G.neighbors(v))).union({v})
    G[u][v]['weight']=len(adjU.intersection(adjV))/min(len(adjU),len(adjV))
   
   
print("similarities calculated ! \n")
 

def Getlist_simlarity(Graph):
    sim_list=[]
    for (u,v,d) in Graph.edges(data=True):
        sim_list.append(d['weight'])
    return list(dict.fromkeys(sim_list))

def Get_Max_Edges_sets(Graph,maxi_weight):
    maxi_edges=[]
    for (u,v,d) in Graph.edges(data=True):
        if d['weight'] == maxi_weight:
            maxi_edges.append((u,v))        
    return maxi_edges



def to_edges(l):
    it = iter(l)
    last = next(it)
    for current in it:
        yield last, current
        last = current 
def to_graph(l):
    gr = networkx.Graph()
    for part in l:
        gr.add_nodes_from(part)
        gr.add_edges_from(to_edges(part))
    return gr

def Merge_edges(List_edges):
    gra = to_graph(List_edges)
    return list(connected_components(gra))
    

def init_commnuities(Graph):
    Com=[]
    for node in Graph.nodes():
        Com.append({node})
    return Com

#(2) detect communities AM method  

print("detecting comms....")
start_time = time.time()
current_clustering_list=init_commnuities(G)
current_modularity=modularity(G,current_clustering_list,weight='weight')
list_weights=Getlist_simlarity(G)
itterations=0
while True:
    if list_weights:
        maxi_weight=max(list_weights)
    else:
        break
    maxi_edges_sets=Get_Max_Edges_sets(G,maxi_weight)
    maxi_edges_sets_merged=list(nx1.connected_components(nx1.Graph(maxi_edges_sets)))
    previous_clustering_list=current_clustering_list
    previous_modularity=current_modularity
    current_clustering_list=Merge_edges(current_clustering_list+maxi_edges_sets_merged)
    itterations+=1
    current_modularity=modularity(G,current_clustering_list,weight='weight')
    if current_modularity<previous_modularity:
        break
    list_weights.remove(maxi_weight)
if current_modularity>=previous_modularity:
    result=current_clustering_list
   
else:
    result=previous_clustering_list
end_time = time.time()
#
#(3) Printing the Number of itterations and the runtime results
print("The running-time = ",end_time-start_time)

print("The number of itteration count = ",itterations)

