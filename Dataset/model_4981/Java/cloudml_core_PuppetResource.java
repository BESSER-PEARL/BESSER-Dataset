





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_PuppetResource extends Resource {

    private String masterEndpoint;
    private String manifestEntry;
    private String username;
    private String repositoryKey;
    private String configurationFile;
    private String repositoryEndpoint;
    private String configureHostnameCommand;



    public cloudml_core_PuppetResource(
        String masterEndpoint,        String manifestEntry,        String username,        String repositoryKey,        String configurationFile,        String repositoryEndpoint,        String configureHostnameCommand    ) {
        super(
        );
        this.masterEndpoint = masterEndpoint;
        this.manifestEntry = manifestEntry;
        this.username = username;
        this.repositoryKey = repositoryKey;
        this.configurationFile = configurationFile;
        this.repositoryEndpoint = repositoryEndpoint;
        this.configureHostnameCommand = configureHostnameCommand;
    }


    public String getMasterendpoint() {
        return masterEndpoint;
    }

    public void setMasterendpoint(String masterEndpoint) {
        this.masterEndpoint = masterEndpoint;
    }
    public String getManifestentry() {
        return manifestEntry;
    }

    public void setManifestentry(String manifestEntry) {
        this.manifestEntry = manifestEntry;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getRepositorykey() {
        return repositoryKey;
    }

    public void setRepositorykey(String repositoryKey) {
        this.repositoryKey = repositoryKey;
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
    public String getConfigurehostnamecommand() {
        return configureHostnameCommand;
    }

    public void setConfigurehostnamecommand(String configureHostnameCommand) {
        this.configureHostnameCommand = configureHostnameCommand;
    }


}