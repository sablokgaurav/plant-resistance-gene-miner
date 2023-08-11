from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
def mineResistanceGenes(id):
    """
    _id : provide the resistance gene id
    a resistance gene miner for the machine learning
    approach. it will automatically connect to the 
    resistance gene database and will fetch the GenBank id
    for sequence download. 
    """
    resistancegene = id
    gene_url = urlopen(f"http://www.prgdb.org/prgdb/genes/type/reference/{resistancegene}")
    resistance_gene_content = ''.join([i for i in ([i.get_text() for 
                                    i in BeautifulSoup(gene_url,"html.parser").
                                        find_all("div", class_ = "row container")]) 
                                                                       if "GenBank" in i])
    resistance_gene_genbank = ''.join(list(filter(None,[''.join(re.findall
                                            (r'[0-9]',i)) for i in [i for i in 
                                                            resistance_gene_content.split() 
                                                                        if "GenBank" in i]])))
    return resistance_gene_genbank
