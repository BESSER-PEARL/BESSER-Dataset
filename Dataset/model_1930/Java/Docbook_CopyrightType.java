





import java.util.List;
import java.util.ArrayList;

public class Docbook_CopyrightType  {

    private String group;
    private String holder;
    private String year;





    private Docbook_InfoType docbook_infotype;


    public Docbook_CopyrightType(
        String group,        String holder,        String year    ) {
        this.group = group;
        this.holder = holder;
        this.year = year;
    }


    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getHolder() {
        return holder;
    }

    public void setHolder(String holder) {
        this.holder = holder;
    }
    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }

    public Docbook_InfoType getDocbook_infotype() {
        return docbook_infotype;
    }

    public void setDocbook_infotype(Docbook_InfoType docbook_infotype) {
        this.docbook_infotype = docbook_infotype;
    }

}