





import java.util.List;
import java.util.ArrayList;

public class FEEDBACK  {

    private String like;
    private String createdAt;
    private String updateAt;
    private String linkInstagram;
    private String productId;
    private String photos;
    private String linkYoutube;
    private String _id;
    private String userId;
    private String wysiwyg;





    private USER user;


    public FEEDBACK(
        String like,        String createdAt,        String updateAt,        String linkInstagram,        String productId,        String photos,        String linkYoutube,        String _id,        String userId,        String wysiwyg    ) {
        this.like = like;
        this.createdAt = createdAt;
        this.updateAt = updateAt;
        this.linkInstagram = linkInstagram;
        this.productId = productId;
        this.photos = photos;
        this.linkYoutube = linkYoutube;
        this._id = _id;
        this.userId = userId;
        this.wysiwyg = wysiwyg;
    }


    public String getLike() {
        return like;
    }

    public void setLike(String like) {
        this.like = like;
    }
    public String getCreatedat() {
        return createdAt;
    }

    public void setCreatedat(String createdAt) {
        this.createdAt = createdAt;
    }
    public String getUpdateat() {
        return updateAt;
    }

    public void setUpdateat(String updateAt) {
        this.updateAt = updateAt;
    }
    public String getLinkinstagram() {
        return linkInstagram;
    }

    public void setLinkinstagram(String linkInstagram) {
        this.linkInstagram = linkInstagram;
    }
    public String getProductid() {
        return productId;
    }

    public void setProductid(String productId) {
        this.productId = productId;
    }
    public String getPhotos() {
        return photos;
    }

    public void setPhotos(String photos) {
        this.photos = photos;
    }
    public String getLinkyoutube() {
        return linkYoutube;
    }

    public void setLinkyoutube(String linkYoutube) {
        this.linkYoutube = linkYoutube;
    }
    public String get_id() {
        return _id;
    }

    public void set_id(String _id) {
        this._id = _id;
    }
    public String getUserid() {
        return userId;
    }

    public void setUserid(String userId) {
        this.userId = userId;
    }
    public String getWysiwyg() {
        return wysiwyg;
    }

    public void setWysiwyg(String wysiwyg) {
        this.wysiwyg = wysiwyg;
    }

    public USER getUser() {
        return user;
    }

    public void setUser(USER user) {
        this.user = user;
    }

}