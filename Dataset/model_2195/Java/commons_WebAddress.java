





import java.util.List;
import java.util.ArrayList;

public class commons_WebAddress extends Expandable, ResourceAware, Positionable, BundleAware {

    private String secureSkinUri;
    private String jsUri;
    private String baseUri;
    private String imagesUri;
    private String apiPath;
    private String skinUri;
    private String secureImagesUri;
    private String basePath;
    private String secureBaseUri;
    private String secureJsUri;



    public commons_WebAddress(
        String secureSkinUri,        String jsUri,        String baseUri,        String imagesUri,        String apiPath,        String skinUri,        String secureImagesUri,        String basePath,        String secureBaseUri,        String secureJsUri    ) {
        super(
        );
        this.secureSkinUri = secureSkinUri;
        this.jsUri = jsUri;
        this.baseUri = baseUri;
        this.imagesUri = imagesUri;
        this.apiPath = apiPath;
        this.skinUri = skinUri;
        this.secureImagesUri = secureImagesUri;
        this.basePath = basePath;
        this.secureBaseUri = secureBaseUri;
        this.secureJsUri = secureJsUri;
    }


    public String getSecureskinuri() {
        return secureSkinUri;
    }

    public void setSecureskinuri(String secureSkinUri) {
        this.secureSkinUri = secureSkinUri;
    }
    public String getJsuri() {
        return jsUri;
    }

    public void setJsuri(String jsUri) {
        this.jsUri = jsUri;
    }
    public String getBaseuri() {
        return baseUri;
    }

    public void setBaseuri(String baseUri) {
        this.baseUri = baseUri;
    }
    public String getImagesuri() {
        return imagesUri;
    }

    public void setImagesuri(String imagesUri) {
        this.imagesUri = imagesUri;
    }
    public String getApipath() {
        return apiPath;
    }

    public void setApipath(String apiPath) {
        this.apiPath = apiPath;
    }
    public String getSkinuri() {
        return skinUri;
    }

    public void setSkinuri(String skinUri) {
        this.skinUri = skinUri;
    }
    public String getSecureimagesuri() {
        return secureImagesUri;
    }

    public void setSecureimagesuri(String secureImagesUri) {
        this.secureImagesUri = secureImagesUri;
    }
    public String getBasepath() {
        return basePath;
    }

    public void setBasepath(String basePath) {
        this.basePath = basePath;
    }
    public String getSecurebaseuri() {
        return secureBaseUri;
    }

    public void setSecurebaseuri(String secureBaseUri) {
        this.secureBaseUri = secureBaseUri;
    }
    public String getSecurejsuri() {
        return secureJsUri;
    }

    public void setSecurejsuri(String secureJsUri) {
        this.secureJsUri = secureJsUri;
    }


}