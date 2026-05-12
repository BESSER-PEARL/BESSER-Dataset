





import java.util.List;
import java.util.ArrayList;

public class requirementEngineeringLanguage_View  {

    private String name;
    private String desc;





    private requirementEngineeringLanguage_When requirementengineeringlanguage_when;


    public requirementEngineeringLanguage_View(
        String name,        String desc    ) {
        this.name = name;
        this.desc = desc;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDesc() {
        return desc;
    }

    public void setDesc(String desc) {
        this.desc = desc;
    }

    public requirementEngineeringLanguage_When getRequirementengineeringlanguage_when() {
        return requirementengineeringlanguage_when;
    }

    public void setRequirementengineeringlanguage_when(requirementEngineeringLanguage_When requirementengineeringlanguage_when) {
        this.requirementengineeringlanguage_when = requirementengineeringlanguage_when;
    }

}