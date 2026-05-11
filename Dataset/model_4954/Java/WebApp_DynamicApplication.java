





import java.util.List;
import java.util.ArrayList;

public class WebApp_DynamicApplication extends NamedElement {






    private List<WebApp_Pages> webapp_pagess;


    public WebApp_DynamicApplication(
    ) {
        super(
        );
        this.webapp_pagess = new ArrayList<>();
    }

    public WebApp_DynamicApplication(
        ArrayList<WebApp_Pages> webapp_pagess    ) {
        this.webapp_pagess = webapp_pagess;
    }


    public List<WebApp_Pages> getWebapp_pagess() {
        return webapp_pagess;
    }

    public void addWebapp_pages(Webapp_pages webapp_pages) {
        this.webapp_pagess.add(webapp_pages);
    }

}