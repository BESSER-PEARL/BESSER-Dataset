





import java.util.List;
import java.util.ArrayList;

public class eJSL_ComponentReference  {

    private String core;





    private eJSL_Component ejsl_component;




    private eJSL_PageReference ejsl_pagereference;


    public eJSL_ComponentReference(
        String core    ) {
        this.core = core;
    }


    public String getCore() {
        return core;
    }

    public void setCore(String core) {
        this.core = core;
    }

    public eJSL_Component getEjsl_component() {
        return ejsl_component;
    }

    public void setEjsl_component(eJSL_Component ejsl_component) {
        this.ejsl_component = ejsl_component;
    }
    public eJSL_PageReference getEjsl_pagereference() {
        return ejsl_pagereference;
    }

    public void setEjsl_pagereference(eJSL_PageReference ejsl_pagereference) {
        this.ejsl_pagereference = ejsl_pagereference;
    }

}