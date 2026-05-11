





import java.util.List;
import java.util.ArrayList;

public class forms_Condition  {

    private String type;
    private String conditionID;





    private forms_PageElement forms_pageelement;




    private forms_Page forms_page;


    public forms_Condition(
        String type,        String conditionID    ) {
        this.type = type;
        this.conditionID = conditionID;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getConditionid() {
        return conditionID;
    }

    public void setConditionid(String conditionID) {
        this.conditionID = conditionID;
    }

    public forms_PageElement getForms_pageelement() {
        return forms_pageelement;
    }

    public void setForms_pageelement(forms_PageElement forms_pageelement) {
        this.forms_pageelement = forms_pageelement;
    }
    public forms_Page getForms_page() {
        return forms_page;
    }

    public void setForms_page(forms_Page forms_page) {
        this.forms_page = forms_page;
    }

}