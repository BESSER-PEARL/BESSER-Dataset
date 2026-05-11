





import java.util.List;
import java.util.ArrayList;

public class service_syntax_Endpoint  {

    private String location;
    private String name;





    private Binding binding;


    public service_syntax_Endpoint(
        String location,        String name    ) {
        this.location = location;
        this.name = name;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Binding getBinding() {
        return binding;
    }

    public void setBinding(Binding binding) {
        this.binding = binding;
    }

}