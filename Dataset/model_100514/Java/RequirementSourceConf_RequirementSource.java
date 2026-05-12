





import java.util.List;
import java.util.ArrayList;

public class RequirementSourceConf_RequirementSource  {

    private String connectorId;
    private String destinationURI;
    private String dataModelURI;
    private String name;
    private String repositoryURI;





    private RequirementSourceConf_RequirementSources requirementsourceconf_requirementsources;




    private RequirementSourceConf_RequirementsContainer requirementsourceconf_requirementscontainer;


    public RequirementSourceConf_RequirementSource(
        String connectorId,        String destinationURI,        String dataModelURI,        String name,        String repositoryURI    ) {
        this.connectorId = connectorId;
        this.destinationURI = destinationURI;
        this.dataModelURI = dataModelURI;
        this.name = name;
        this.repositoryURI = repositoryURI;
    }


    public String getConnectorid() {
        return connectorId;
    }

    public void setConnectorid(String connectorId) {
        this.connectorId = connectorId;
    }
    public String getDestinationuri() {
        return destinationURI;
    }

    public void setDestinationuri(String destinationURI) {
        this.destinationURI = destinationURI;
    }
    public String getDatamodeluri() {
        return dataModelURI;
    }

    public void setDatamodeluri(String dataModelURI) {
        this.dataModelURI = dataModelURI;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getRepositoryuri() {
        return repositoryURI;
    }

    public void setRepositoryuri(String repositoryURI) {
        this.repositoryURI = repositoryURI;
    }

    public RequirementSourceConf_RequirementSources getRequirementsourceconf_requirementsources() {
        return requirementsourceconf_requirementsources;
    }

    public void setRequirementsourceconf_requirementsources(RequirementSourceConf_RequirementSources requirementsourceconf_requirementsources) {
        this.requirementsourceconf_requirementsources = requirementsourceconf_requirementsources;
    }
    public RequirementSourceConf_RequirementsContainer getRequirementsourceconf_requirementscontainer() {
        return requirementsourceconf_requirementscontainer;
    }

    public void setRequirementsourceconf_requirementscontainer(RequirementSourceConf_RequirementsContainer requirementsourceconf_requirementscontainer) {
        this.requirementsourceconf_requirementscontainer = requirementsourceconf_requirementscontainer;
    }

}