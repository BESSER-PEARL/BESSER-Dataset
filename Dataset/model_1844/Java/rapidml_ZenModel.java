





import java.util.List;
import java.util.ArrayList;

public class rapidml_ZenModel extends Extensible, Documentable, HasTitle {

    private String name;
    private String namespace;





    private List<rapidml_ResourceAPI> rapidml_resourceapis;


    public rapidml_ZenModel(
        String name,        String namespace    ) {
        super(
        );
        this.name = name;
        this.namespace = namespace;
        this.rapidml_resourceapis = new ArrayList<>();
    }

    public rapidml_ZenModel(
        String name,        String namespace        ArrayList<rapidml_ResourceAPI> rapidml_resourceapis    ) {
        this.name = name;
        this.namespace = namespace;
        this.rapidml_resourceapis = rapidml_resourceapis;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
    }

    public List<rapidml_ResourceAPI> getRapidml_resourceapis() {
        return rapidml_resourceapis;
    }

    public void addRapidml_resourceapi(Rapidml_resourceapi rapidml_resourceapi) {
        this.rapidml_resourceapis.add(rapidml_resourceapi);
    }

}