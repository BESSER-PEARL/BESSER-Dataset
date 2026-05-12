





import java.util.List;
import java.util.ArrayList;

public class Magazine  {

    private String location;
    private int issueNum;
    private String name;



    public Magazine(
        String location,        int issueNum,        String name    ) {
        this.location = location;
        this.issueNum = issueNum;
        this.name = name;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public int getIssuenum() {
        return issueNum;
    }

    public void setIssuenum(int issueNum) {
        this.issueNum = issueNum;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}