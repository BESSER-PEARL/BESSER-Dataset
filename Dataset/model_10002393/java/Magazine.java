





import java.util.List;
import java.util.ArrayList;

public class Magazine  {

    private String location;
    private String name;
    private int issueNum;



    public Magazine(
        String location,        String name,        int issueNum    ) {
        this.location = location;
        this.name = name;
        this.issueNum = issueNum;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getIssuenum() {
        return issueNum;
    }

    public void setIssuenum(int issueNum) {
        this.issueNum = issueNum;
    }


}