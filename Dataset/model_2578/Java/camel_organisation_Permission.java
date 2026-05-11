




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class camel_organisation_Permission  {

    private String action;
    private LocalDate endTime;
    private LocalDate startTime;
    private String name;





    private Role role;




    private ResourceFilter resourcefilter;


    public camel_organisation_Permission(
        String action,        LocalDate endTime,        LocalDate startTime,        String name    ) {
        this.action = action;
        this.endTime = endTime;
        this.startTime = startTime;
        this.name = name;
    }


    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }
    public LocalDate getEndtime() {
        return endTime;
    }

    public void setEndtime(LocalDate endTime) {
        this.endTime = endTime;
    }
    public LocalDate getStarttime() {
        return startTime;
    }

    public void setStarttime(LocalDate startTime) {
        this.startTime = startTime;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Role getRole() {
        return role;
    }

    public void setRole(Role role) {
        this.role = role;
    }
    public ResourceFilter getResourcefilter() {
        return resourcefilter;
    }

    public void setResourcefilter(ResourceFilter resourcefilter) {
        this.resourcefilter = resourcefilter;
    }

}