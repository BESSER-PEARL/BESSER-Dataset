





import java.util.List;
import java.util.ArrayList;

public class addressbook_Company extends Contact {

    private String Industry;



    public addressbook_Company(
        String Industry    ) {
        super(
        );
        this.Industry = Industry;
    }


    public String getIndustry() {
        return Industry;
    }

    public void setIndustry(String Industry) {
        this.Industry = Industry;
    }


}