





import java.util.List;
import java.util.ArrayList;

public class RootElement_Staff extends SupportTicketWriter, Cleaning, SupportTicketReader {

    private String name;
    private String staffID;



    public RootElement_Staff(
        String name,        String staffID    ) {
        super(
        );
        this.name = name;
        this.staffID = staffID;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getStaffid() {
        return staffID;
    }

    public void setStaffid(String staffID) {
        this.staffID = staffID;
    }


}