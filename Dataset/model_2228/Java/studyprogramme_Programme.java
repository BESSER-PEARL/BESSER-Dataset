





import java.util.List;
import java.util.ArrayList;

public class studyprogramme_Programme extends SemesterContainer {

    private String programmeType;
    private String name;
    private String programmeCode;
    private int numberOfYears;



    public studyprogramme_Programme(
        String programmeType,        String name,        String programmeCode,        int numberOfYears    ) {
        super(
        );
        this.programmeType = programmeType;
        this.name = name;
        this.programmeCode = programmeCode;
        this.numberOfYears = numberOfYears;
    }


    public String getProgrammetype() {
        return programmeType;
    }

    public void setProgrammetype(String programmeType) {
        this.programmeType = programmeType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getProgrammecode() {
        return programmeCode;
    }

    public void setProgrammecode(String programmeCode) {
        this.programmeCode = programmeCode;
    }
    public int getNumberofyears() {
        return numberOfYears;
    }

    public void setNumberofyears(int numberOfYears) {
        this.numberOfYears = numberOfYears;
    }


}