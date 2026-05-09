





import java.util.List;
import java.util.ArrayList;

public class myDsl_DataPersistenceContent  {






    private myDsl_DataPersistenceLayer mydsl_datapersistencelayer;




    private List<myDsl_DataPersistenceSegments> mydsl_datapersistencesegmentss;


    public myDsl_DataPersistenceContent(
    ) {
        this.mydsl_datapersistencesegmentss = new ArrayList<>();
    }

    public myDsl_DataPersistenceContent(
        ArrayList<myDsl_DataPersistenceSegments> mydsl_datapersistencesegmentss    ) {
        this.mydsl_datapersistencesegmentss = mydsl_datapersistencesegmentss;
    }


    public myDsl_DataPersistenceLayer getMydsl_datapersistencelayer() {
        return mydsl_datapersistencelayer;
    }

    public void setMydsl_datapersistencelayer(myDsl_DataPersistenceLayer mydsl_datapersistencelayer) {
        this.mydsl_datapersistencelayer = mydsl_datapersistencelayer;
    }
    public List<myDsl_DataPersistenceSegments> getMydsl_datapersistencesegmentss() {
        return mydsl_datapersistencesegmentss;
    }

    public void addMydsl_datapersistencesegments(Mydsl_datapersistencesegments mydsl_datapersistencesegments) {
        this.mydsl_datapersistencesegmentss.add(mydsl_datapersistencesegments);
    }

}