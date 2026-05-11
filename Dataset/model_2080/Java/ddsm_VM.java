





import java.util.List;
import java.util.ArrayList;

public class ddsm_VM extends ExternalComponent {

    private String providerSpecificTypeName;
    private String minRam;
    private String genericSize;
    private int publicPorts;
    private String os;
    private String minCores;
    private String minStorage;
    private String maxRam;
    private String maxStorage;
    private int instances;
    private String securityGroup;
    private String is64os;
    private String privateKey;
    private String sshKey;
    private String imageId;
    private String publicAddress;
    private String maxCores;



    public ddsm_VM(
        String providerSpecificTypeName,        String minRam,        String genericSize,        int publicPorts,        String os,        String minCores,        String minStorage,        String maxRam,        String maxStorage,        int instances,        String securityGroup,        String is64os,        String privateKey,        String sshKey,        String imageId,        String publicAddress,        String maxCores    ) {
        super(
        );
        this.providerSpecificTypeName = providerSpecificTypeName;
        this.minRam = minRam;
        this.genericSize = genericSize;
        this.publicPorts = publicPorts;
        this.os = os;
        this.minCores = minCores;
        this.minStorage = minStorage;
        this.maxRam = maxRam;
        this.maxStorage = maxStorage;
        this.instances = instances;
        this.securityGroup = securityGroup;
        this.is64os = is64os;
        this.privateKey = privateKey;
        this.sshKey = sshKey;
        this.imageId = imageId;
        this.publicAddress = publicAddress;
        this.maxCores = maxCores;
    }


    public String getProviderspecifictypename() {
        return providerSpecificTypeName;
    }

    public void setProviderspecifictypename(String providerSpecificTypeName) {
        this.providerSpecificTypeName = providerSpecificTypeName;
    }
    public String getMinram() {
        return minRam;
    }

    public void setMinram(String minRam) {
        this.minRam = minRam;
    }
    public String getGenericsize() {
        return genericSize;
    }

    public void setGenericsize(String genericSize) {
        this.genericSize = genericSize;
    }
    public int getPublicports() {
        return publicPorts;
    }

    public void setPublicports(int publicPorts) {
        this.publicPorts = publicPorts;
    }
    public String getOs() {
        return os;
    }

    public void setOs(String os) {
        this.os = os;
    }
    public String getMincores() {
        return minCores;
    }

    public void setMincores(String minCores) {
        this.minCores = minCores;
    }
    public String getMinstorage() {
        return minStorage;
    }

    public void setMinstorage(String minStorage) {
        this.minStorage = minStorage;
    }
    public String getMaxram() {
        return maxRam;
    }

    public void setMaxram(String maxRam) {
        this.maxRam = maxRam;
    }
    public String getMaxstorage() {
        return maxStorage;
    }

    public void setMaxstorage(String maxStorage) {
        this.maxStorage = maxStorage;
    }
    public int getInstances() {
        return instances;
    }

    public void setInstances(int instances) {
        this.instances = instances;
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
    public String getImageid() {
        return imageId;
    }

    public void setImageid(String imageId) {
        this.imageId = imageId;
    }
    public String getPublicaddress() {
        return publicAddress;
    }

    public void setPublicaddress(String publicAddress) {
        this.publicAddress = publicAddress;
    }
    public String getMaxcores() {
        return maxCores;
    }

    public void setMaxcores(String maxCores) {
        this.maxCores = maxCores;
    }


}