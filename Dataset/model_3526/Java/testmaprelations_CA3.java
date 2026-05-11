





import java.util.List;
import java.util.ArrayList;

public class testmaprelations_CA3  {






    private List<testmaprelations_MapCA3ToCB3MapEntry> testmaprelations_mapca3tocb3mapentrys;




    private testmaprelations_MapCA3ToCB3MapEntry testmaprelations_mapca3tocb3mapentry;


    public testmaprelations_CA3(
    ) {
        this.testmaprelations_mapca3tocb3mapentrys = new ArrayList<>();
    }

    public testmaprelations_CA3(
        ArrayList<testmaprelations_MapCA3ToCB3MapEntry> testmaprelations_mapca3tocb3mapentrys    ) {
        this.testmaprelations_mapca3tocb3mapentrys = testmaprelations_mapca3tocb3mapentrys;
    }


    public List<testmaprelations_MapCA3ToCB3MapEntry> getTestmaprelations_mapca3tocb3mapentrys() {
        return testmaprelations_mapca3tocb3mapentrys;
    }

    public void addTestmaprelations_mapca3tocb3mapentry(Testmaprelations_mapca3tocb3mapentry testmaprelations_mapca3tocb3mapentry) {
        this.testmaprelations_mapca3tocb3mapentrys.add(testmaprelations_mapca3tocb3mapentry);
    }
    public testmaprelations_MapCA3ToCB3MapEntry getTestmaprelations_mapca3tocb3mapentry() {
        return testmaprelations_mapca3tocb3mapentry;
    }

    public void setTestmaprelations_mapca3tocb3mapentry(testmaprelations_MapCA3ToCB3MapEntry testmaprelations_mapca3tocb3mapentry) {
        this.testmaprelations_mapca3tocb3mapentry = testmaprelations_mapca3tocb3mapentry;
    }

}