





import java.util.List;
import java.util.ArrayList;

public class cloudml_PuppetResource extends Resource {

    private String configurationFile;
    private String configureHostnameCommand;
    private String repositoryKey;
    private String masterEndpoint;
    private String repositoryEndpoint;
    private String username;
    private String manifestEntry;



    public cloudml_PuppetResource(
        String configurationFile,        String configureHostnameCommand,        String repositoryKey,        String masterEndpoint,        String repositoryEndpoint,        String username,        String manifestEntry    ) {
        super(
        );
        this.configurationFile = configurationFile;
        this.configureHostnameCommand = configureHostnameCommand;
        this.repositoryKey = repositoryKey;
        this.masterEndpoint = masterEndpoint;
        this.repositoryEndpoint = repositoryEndpoint;
        this.username = username;
        this.manifestEntry = manifestEntry;
    }


    public String getConfigurationfile() {
        return configurationFile;
    }

    public void setConfigurationfile(String configurationFile) {
        this.configurationFile = configurationFile;
    }
    public String getConfigurehostnamecommand() {
        return configureHostnameCommand;
    }

    public void setConfigurehostnamecommand(String configureHostnameCommand) {
        this.configureHostnameCommand = configureHostnameCommand;
    }
    public String getRepositorykey() {
        return repositoryKey;
    }

    public void setRepositorykey(String repositoryKey) {
        this.repositoryKey = repositoryKey;
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


}