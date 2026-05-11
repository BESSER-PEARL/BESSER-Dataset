





import java.util.List;
import java.util.ArrayList;

public class DiagonosticModel_SignalType  {

    private String lookupValues;
    private String MessageName;
    private String creationMode;
    private String node;
    private String type;
    private String name;
    private String namespace;





    private DiagonosticModel_TestStep diagonosticmodel_teststep;




    private DiagonosticModel_ImportArtifact diagonosticmodel_importartifact;


    public DiagonosticModel_SignalType(
        String lookupValues,        String MessageName,        String creationMode,        String node,        String type,        String name,        String namespace    ) {
        this.lookupValues = lookupValues;
        this.MessageName = MessageName;
        this.creationMode = creationMode;
        this.node = node;
        this.type = type;
        this.name = name;
        this.namespace = namespace;
    }


    public String getLookupvalues() {
        return lookupValues;
    }

    public void setLookupvalues(String lookupValues) {
        this.lookupValues = lookupValues;
    }
    public String getMessagename() {
        return MessageName;
    }

    public void setMessagename(String MessageName) {
        this.MessageName = MessageName;
    }
    public String getCreationmode() {
        return creationMode;
    }

    public void setCreationmode(String creationMode) {
        this.creationMode = creationMode;
    }
    public String getNode() {
        return node;
    }

    public void setNode(String node) {
        this.node = node;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
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

    public DiagonosticModel_TestStep getDiagonosticmodel_teststep() {
        return diagonosticmodel_teststep;
    }

    public void setDiagonosticmodel_teststep(DiagonosticModel_TestStep diagonosticmodel_teststep) {
        this.diagonosticmodel_teststep = diagonosticmodel_teststep;
    }
    public DiagonosticModel_ImportArtifact getDiagonosticmodel_importartifact() {
        return diagonosticmodel_importartifact;
    }

    public void setDiagonosticmodel_importartifact(DiagonosticModel_ImportArtifact diagonosticmodel_importartifact) {
        this.diagonosticmodel_importartifact = diagonosticmodel_importartifact;
    }

}