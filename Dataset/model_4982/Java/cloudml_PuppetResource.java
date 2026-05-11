





import java.util.List;
import java.util.ArrayList;

public class cloudml_PuppetResource extends Resource {

    private String masterEndpoint;
    private String repositoryEndpoint;
    private String username;
    private String manifestEntry;
    private String configurationFile;
    private String repositoryKey;
    private String configureHostnameCommand;



    public cloudml_PuppetResource(
        String masterEndpoint,        String repositoryEndpoint,        String username,        String manifestEntry,        String configurationFile,        String repositoryKey,        String configureHostnameCommand    ) {
        super(
        );
        this.masterEndpoint = masterEndpoint;
        this.repositoryEndpoint = repositoryEndpoint;
        this.username = username;
        this.manifestEntry = manifestEntry;
        this.configurationFile = configurationFile;
        this.repositoryKey = repositoryKey;
        this.configureHostnameCommand = configureHostnameCommand;
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
    public String getManifestentry() {
        return manifestEntry;
    }

    public void setManifestentry(String manifestEntry) {
        this.manifestEntry = manifestEntry;
    }
    public String getConfigurationfile() {
        return configurationFile;
    }

    public void setConfigurationfile(String configurationFile) {
        this.configurationFile = configurationFile;
    }
    public String getRepositorykey() {
        return repositoryKey;
    }

    public void setRepositorykey(String repositoryKey) {
        this.repositoryKey = repositoryKey;
    }
    public String getConfigurehostnamecommand() {
        return configureHostnameCommand;
    }

    public void setConfigurehostnamecommand(String configureHostnameCommand) {
        this.configureHostnameCommand = configureHostnameCommand;
    }


}