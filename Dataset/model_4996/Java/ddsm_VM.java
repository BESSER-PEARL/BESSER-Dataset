





import java.util.List;
import java.util.ArrayList;

public class ddsm_VM extends ExternalComponent {

    private String instances;
    private String maxCores;
    private String publicAddress;
    private String minRam;
    private String minStorage;
    private String minCores;
    private String os;
    private String publicPorts;
    private String imageId;
    private String providerSpecificTypeName;
    private String genericSize;
    private String maxStorage;
    private String securityGroup;
    private String is64os;
    private String privateKey;
    private String sshKey;
    private String maxRam;



    public ddsm_VM(
        String instances,        String maxCores,        String publicAddress,        String minRam,        String minStorage,        String minCores,        String os,        String publicPorts,        String imageId,        String providerSpecificTypeName,        String genericSize,        String maxStorage,        String securityGroup,        String is64os,        String privateKey,        String sshKey,        String maxRam    ) {
        super(
        );
        this.instances = instances;
        this.maxCores = maxCores;
        this.publicAddress = publicAddress;
        this.minRam = minRam;
        this.minStorage = minStorage;
        this.minCores = minCores;
        this.os = os;
        this.publicPorts = publicPorts;
        this.imageId = imageId;
        this.providerSpecificTypeName = providerSpecificTypeName;
        this.genericSize = genericSize;
        this.maxStorage = maxStorage;
        this.securityGroup = securityGroup;
        this.is64os = is64os;
        this.privateKey = privateKey;
        this.sshKey = sshKey;
        this.maxRam = maxRam;
    }


    public String getInstances() {
        return instances;
    }

    public void setInstances(String instances) {
        this.instances = instances;
    }
    public String getMaxcores() {
        return maxCores;
    }

    public void setMaxcores(String maxCores) {
        this.maxCores = maxCores;
    }
    public String getPublicaddress() {
        return publicAddress;
    }

    public void setPublicaddress(String publicAddress) {
        this.publicAddress = publicAddress;
    }
    public String getMinram() {
        return minRam;
    }

    public void setMinram(String minRam) {
        this.minRam = minRam;
    }
    public String getMinstorage() {
        return minStorage;
    }

    public void setMinstorage(String minStorage) {
        this.minStorage = minStorage;
    }
    public String getMincores() {
        return minCores;
    }

    public void setMincores(String minCores) {
        this.minCores = minCores;
    }
    public String getOs() {
        return os;
    }

    public void setOs(String os) {
        this.os = os;
    }
    public String getPublicports() {
        return publicPorts;
    }

    public void setPublicports(String publicPorts) {
        this.publicPorts = publicPorts;
    }
    public String getImageid() {
        return imageId;
    }

    public void setImageid(String imageId) {
        this.imageId = imageId;
    }
    public String getProviderspecifictypename() {
        return providerSpecificTypeName;
    }

    public void setProviderspecifictypename(String providerSpecificTypeName) {
        this.providerSpecificTypeName = providerSpecificTypeName;
    }
    public String getGenericsize() {
        return genericSize;
    }

    public void setGenericsize(String genericSize) {
        this.genericSize = genericSize;
    }
    public String getMaxstorage() {
        return maxStorage;
    }

    public void setMaxstorage(String maxStorage) {
        this.maxStorage = maxStorage;
    }
    public String getSecuritygroup() {
        return securityGroup;
    }

    public void setSecuritygroup(String securityGroup) {
        this.securityGroup = securityGroup;
    }
    public String getIs64os() {
        return is64os;
    }

    public void setIs64os(String is64os) {
        this.is64os = is64os;
    }
    public String getPrivatekey() {
        return privateKey;
    }

    public void setPrivatekey(String privateKey) {
        this.privateKey = privateKey;
    }
    public String getSshkey() {
        return sshKey;
    }

    public void setSshkey(String sshKey) {
        this.sshKey = sshKey;
    }
    public String getMaxram() {
        return maxRam;
    }

    public void setMaxram(String maxRam) {
        this.maxRam = maxRam;
    }


}