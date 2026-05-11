





import java.util.List;
import java.util.ArrayList;

public class Service_JavaService  {

    private String option;
    private String name;





    private Service_Tool service_tool;


    public Service_JavaService(
        String option,        String name    ) {
        this.option = option;
        this.name = name;
    }


    public String getOption() {
        return option;
    }

    public void setOption(String option) {
        this.option = option;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Service_Tool getService_tool() {
        return service_tool;
    }

    public void setService_tool(Service_Tool service_tool) {
        this.service_tool = service_tool;
    }

}