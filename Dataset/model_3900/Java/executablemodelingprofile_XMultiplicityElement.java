





import java.util.List;
import java.util.ArrayList;

public class executablemodelingprofile_XMultiplicityElement  {

    private String isDescending;
    private String isOrderedByValue;





    private List<executablemodelingprofile_Property> executablemodelingprofile_propertys;


    public executablemodelingprofile_XMultiplicityElement(
        String isDescending,        String isOrderedByValue    ) {
        this.isDescending = isDescending;
        this.isOrderedByValue = isOrderedByValue;
        this.executablemodelingprofile_propertys = new ArrayList<>();
    }

    public executablemodelingprofile_XMultiplicityElement(
        String isDescending,        String isOrderedByValue        ArrayList<executablemodelingprofile_Property> executablemodelingprofile_propertys    ) {
        this.isDescending = isDescending;
        this.isOrderedByValue = isOrderedByValue;
        this.executablemodelingprofile_propertys = executablemodelingprofile_propertys;
    }

    public String getIsdescending() {
        return isDescending;
    }

    public void setIsdescending(String isDescending) {
        this.isDescending = isDescending;
    }
    public String getIsorderedbyvalue() {
        return isOrderedByValue;
    }

    public void setIsorderedbyvalue(String isOrderedByValue) {
        this.isOrderedByValue = isOrderedByValue;
    }

    public List<executablemodelingprofile_Property> getExecutablemodelingprofile_propertys() {
        return executablemodelingprofile_propertys;
    }

    public void addExecutablemodelingprofile_property(Executablemodelingprofile_property executablemodelingprofile_property) {
        this.executablemodelingprofile_propertys.add(executablemodelingprofile_property);
    }

}