





import java.util.List;
import java.util.ArrayList;

public class maven_Mappings  {






    private List<maven_MapEntry> maven_mapentrys;




    private maven_MavenProvider maven_mavenprovider;


    public maven_Mappings(
    ) {
        this.maven_mapentrys = new ArrayList<>();
    }

    public maven_Mappings(
        ArrayList<maven_MapEntry> maven_mapentrys    ) {
        this.maven_mapentrys = maven_mapentrys;
    }


    public List<maven_MapEntry> getMaven_mapentrys() {
        return maven_mapentrys;
    }

    public void addMaven_mapentry(Maven_mapentry maven_mapentry) {
        this.maven_mapentrys.add(maven_mapentry);
    }
    public maven_MavenProvider getMaven_mavenprovider() {
        return maven_mavenprovider;
    }

    public void setMaven_mavenprovider(maven_MavenProvider maven_mavenprovider) {
        this.maven_mavenprovider = maven_mavenprovider;
    }

}