





import java.util.List;
import java.util.ArrayList;

public class rapidml_NamedLinkDescriptor extends ObjectRealization {

    private boolean default;
    private String name;





    private rapidml_ServiceDataResource rapidml_servicedataresource;


    public rapidml_NamedLinkDescriptor(
        boolean default,        String name    ) {
        super(
        );
        this.default = default;
        this.name = name;
    }


    public boolean getDefault() {
        return default;
    }

    public void setDefault(boolean default) {
        this.default = default;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public rapidml_ServiceDataResource getRapidml_servicedataresource() {
        return rapidml_servicedataresource;
    }

    public void setRapidml_servicedataresource(rapidml_ServiceDataResource rapidml_servicedataresource) {
        this.rapidml_servicedataresource = rapidml_servicedataresource;
    }

}