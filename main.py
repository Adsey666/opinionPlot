from opinionPlot import OpinionPlot
import nltk


###################################################
#                  Main Definition                #
###################################################
def main():
    """ Main """
    op = OpinionPlot("testData.txt") #TODO: explain what is testData? so each person has a 2 number ranking...
    op.plotOpinions("Opinions") #TODO: what do they range from good or bad? guess dm because just seeing how clustered
    op.plotAvgOpinions("Average Opinions")
    op.plotClusters("Clusters", 3)
    op.showPlots()


##################################################
#                   Call Main                    #
##################################################
if __name__ == '__main__':
    main()