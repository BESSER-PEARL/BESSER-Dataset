





import java.util.List;
import java.util.ArrayList;

public class eSport_League  {

    private int size;
    private String name;
    private String season;
    private int year;





    private eSport_GroupStage esport_groupstage;




    private eSport_Zone esport_zone;




    private eSport_Qualification esport_qualification;




    private List<eSport_Qualification> esport_qualifications;




    private eSport_GroupStage esport_groupstage;




    private eSport_Zone esport_zone;


    public eSport_League(
        int size,        String name,        String season,        int year    ) {
        this.size = size;
        this.name = name;
        this.season = season;
        this.year = year;
        this.esport_qualifications = new ArrayList<>();
    }

    public eSport_League(
        int size,        String name,        String season,        int year        ArrayList<eSport_Qualification> esport_qualifications    ) {
        this.size = size;
        this.name = name;
        this.season = season;
        this.year = year;
        this.esport_qualifications = esport_qualifications;
    }

    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSeason() {
        return season;
    }

    public void setSeason(String season) {
        this.season = season;
    }
    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public eSport_GroupStage getEsport_groupstage() {
        return esport_groupstage;
    }

    public void setEsport_groupstage(eSport_GroupStage esport_groupstage) {
        this.esport_groupstage = esport_groupstage;
    }
    public eSport_Zone getEsport_zone() {
        return esport_zone;
    }

    public void setEsport_zone(eSport_Zone esport_zone) {
        this.esport_zone = esport_zone;
    }
    public eSport_Qualification getEsport_qualification() {
        return esport_qualification;
    }

    public void setEsport_qualification(eSport_Qualification esport_qualification) {
        this.esport_qualification = esport_qualification;
    }
    public List<eSport_Qualification> getEsport_qualifications() {
        return esport_qualifications;
    }

    public void addEsport_qualification(Esport_qualification esport_qualification) {
        this.esport_qualifications.add(esport_qualification);
    }
    public eSport_GroupStage getEsport_groupstage() {
        return esport_groupstage;
    }

    public void setEsport_groupstage(eSport_GroupStage esport_groupstage) {
        this.esport_groupstage = esport_groupstage;
    }
    public eSport_Zone getEsport_zone() {
        return esport_zone;
    }

    public void setEsport_zone(eSport_Zone esport_zone) {
        this.esport_zone = esport_zone;
    }

}