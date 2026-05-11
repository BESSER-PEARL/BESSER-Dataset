





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_PuppetResource extends Resource {

    private String repositoryKey;
    private String username;
    private String configurationFile;
    private String repositoryEndpoint;
    private String masterEndpoint;
    private String configureHostnameCommand;
    private String manifestEntry;



    public cloudml_core_PuppetResource(
        String repositoryKey,        String username,        String configurationFile,        String repositoryEndpoint,        String masterEndpoint,        String configureHostnameCommand,        String manifestEntry    ) {
        super(
        );
        this.repositoryKey = repositoryKey;
        this.username = username;
        this.configurationFile = configurationFile;
        this.repositoryEndpoint = repositoryEndpoint;
        this.masterEndpoint = masterEndpoint;
        this.configureHostnameCommand = configureHostnameCommand;
        this.manifestEntry = manifestEntry;
    }


    public String getRepositorykey() {
        return repositoryKey;
    }

    public void setRepositorykey(String repositoryKey) {
        this.repositoryKey = repositoryKey;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getConfigurationfile() {
        return configurationFile;
    }

    public void setConfigurationfile(String configurationFile) {
        this.configurationFile = configurationFile;
    }
    public String getRepositoryendpoint() {
        return repositoryEndpoint;
    }

    public void setRepositoryendpoint(String repositoryEndpoint) {
        this.repositoryEndpoint = repositoryEndpoint;
    }
    public String getMasterendpoint() {
        return masterEndpoint;
    }

    public void setMasterendpoint(String masterEndpoint) {
        this.masterEndpoint = masterEndpoint;
    }
    public String getConfigurehostnamecommand() {
        return configureHostnameCommand;
    }

    public void setConfigurehostnamecommand(String configureHostnameCommand) {
        this.configureHostnameCommand = configureHostnameCommand;
    }
    public String getManifestentry() {
        return manifestEntry;
    }

    public void setManifestentry(String manifestEntry) {
        this.manifestEntry = manifestEntry;
    }


}