





import java.util.List;
import java.util.ArrayList;

public class forms_AttributeValueCondition extends Condition {

    private String value;
    private String type;





    private forms_PageElement forms_pageelement;




    private forms_CompositionCondition forms_compositioncondition;




    private forms_PageElement forms_pageelement;




    private forms_Page forms_page;


    public forms_AttributeValueCondition(
        String value,        String type    ) {
        super(
        );
        this.value = value;
        this.type = type;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public forms_PageElement getForms_pageelement() {
        return forms_pageelement;
    }

    public void setForms_pageelement(forms_PageElement forms_pageelement) {
        this.forms_pageelement = forms_pageelement;
    }
    public forms_CompositionCondition getForms_compositioncondition() {
        return forms_compositioncondition;
    }

    public void setForms_compositioncondition(forms_CompositionCondition forms_compositioncondition) {
        this.forms_compositioncondition = forms_compositioncondition;
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