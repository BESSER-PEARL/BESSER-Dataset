





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_PuppetResource extends Resource {

    private String manifestEntry;
    private String configureHostnameCommand;
    private String configurationFile;
    private String masterEndpoint;
    private String repositoryEndpoint;
    private String username;
    private String repositoryKey;



    public cloudml_core_PuppetResource(
        String manifestEntry,        String configureHostnameCommand,        String configurationFile,        String masterEndpoint,        String repositoryEndpoint,        String username,        String repositoryKey    ) {
        super(
        );
        this.manifestEntry = manifestEntry;
        this.configureHostnameCommand = configureHostnameCommand;
        this.configurationFile = configurationFile;
        this.masterEndpoint = masterEndpoint;
        this.repositoryEndpoint = repositoryEndpoint;
        this.username = username;
        this.repositoryKey = repositoryKey;
    }


    public String getManifestentry() {
        return manifestEntry;
    }

    public void setManifestentry(String manifestEntry) {
        this.manifestEntry = manifestEntry;
    }
    public String getConfigurehostnamecommand() {
        return configureHostnameCommand;
    }

    public void setConfigurehostnamecommand(String configureHostnameCommand) {
        this.configureHostnameCommand = configureHostnameCommand;
    }
    public String getConfigurationfile() {
        return configurationFile;
    }

    public void setConfigurationfile(String configurationFile) {
        this.configurationFile = configurationFile;
    }
    public String getMasterendpoint() {
        return masterEndpoint;
    }

    public void setMasterendpoint(String masterEndpoint) {
        this.masterEndpoint = masterEndpoint;
    }
    public String getRepositoryendpoint() {
        return repositoryEndpoint;
    }

    public void setRepositoryendpoint(String repositoryEndpoint) {
        this.repositoryEndpoint = repositoryEndpoint;
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


}