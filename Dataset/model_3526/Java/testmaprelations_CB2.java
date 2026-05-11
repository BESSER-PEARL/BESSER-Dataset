





import java.util.List;
import java.util.ArrayList;

public class testmaprelations_CB2  {






    private List<testmaprelations_MapCA2ToCB2MapEntry> testmaprelations_mapca2tocb2mapentrys;




    private testmaprelations_MapCA2ToCB2MapEntry testmaprelations_mapca2tocb2mapentry;


    public testmaprelations_CB2(
    ) {
        this.testmaprelations_mapca2tocb2mapentrys = new ArrayList<>();
    }

    public testmaprelations_CB2(
        ArrayList<testmaprelations_MapCA2ToCB2MapEntry> testmaprelations_mapca2tocb2mapentrys    ) {
        this.testmaprelations_mapca2tocb2mapentrys = testmaprelations_mapca2tocb2mapentrys;
    }


    public List<testmaprelations_MapCA2ToCB2MapEntry> getTestmaprelations_mapca2tocb2mapentrys() {
        return testmaprelations_mapca2tocb2mapentrys;
    }

    public void addTestmaprelations_mapca2tocb2mapentry(Testmaprelations_mapca2tocb2mapentry testmaprelations_mapca2tocb2mapentry) {
        this.testmaprelations_mapca2tocb2mapentrys.add(testmaprelations_mapca2tocb2mapentry);
    }
    public testmaprelations_MapCA2ToCB2MapEntry getTestmaprelations_mapca2tocb2mapentry() {
        return testmaprelations_mapca2tocb2mapentry;
    }

    public void setTestmaprelations_mapca2tocb2mapentry(testmaprelations_MapCA2ToCB2MapEntry testmaprelations_mapca2tocb2mapentry) {
        this.testmaprelations_mapca2tocb2mapentry = testmaprelations_mapca2tocb2mapentry;
    }

}