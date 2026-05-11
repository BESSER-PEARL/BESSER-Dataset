





import java.util.List;
import java.util.ArrayList;

public class PhotosMetaModel_AmazonS3API extends Connection {

    private String accessKey;
    private String secretKey;
    private String endpointUrl;
    private String bucketName;



    public PhotosMetaModel_AmazonS3API(
        String accessKey,        String secretKey,        String endpointUrl,        String bucketName    ) {
        super(
        );
        this.accessKey = accessKey;
        this.secretKey = secretKey;
        this.endpointUrl = endpointUrl;
        this.bucketName = bucketName;
    }


    public String getAccesskey() {
        return accessKey;
    }

    public void setAccesskey(String accessKey) {
        this.accessKey = accessKey;
    }
    public String getSecretkey() {
        return secretKey;
    }

    public void setSecretkey(String secretKey) {
        this.secretKey = secretKey;
    }
    public String getEndpointurl() {
        return endpointUrl;
    }

    public void setEndpointurl(String endpointUrl) {
        this.endpointUrl = endpointUrl;
    }
    public String getBucketname() {
        return bucketName;
    }

    public void setBucketname(String bucketName) {
        this.bucketName = bucketName;
    }


}