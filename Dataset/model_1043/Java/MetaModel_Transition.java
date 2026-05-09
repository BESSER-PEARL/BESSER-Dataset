





import java.util.List;
import java.util.ArrayList;

public class MetaModel_Transition  {

    private String description;
    private String name;





    private MetaModel_EvolutionStyle metamodel_evolutionstyle;


    public MetaModel_Transition(
        String description,        String name    ) {
        this.description = description;
        this.name = name;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public MetaModel_EvolutionStyle getMetamodel_evolutionstyle() {
        return metamodel_evolutionstyle;
    }

    public void setMetamodel_evolutionstyle(MetaModel_EvolutionStyle metamodel_evolutionstyle) {
        this.metamodel_evolutionstyle = metamodel_evolutionstyle;
    }

}