





import java.util.List;
import java.util.ArrayList;

public class frameweb_DomainAssociation extends Association {

    private String order;
    private String fetch;
    private String collection;
    private String cascade;



    public frameweb_DomainAssociation(
        String order,        String fetch,        String collection,        String cascade    ) {
        super(
        );
        this.order = order;
        this.fetch = fetch;
        this.collection = collection;
        this.cascade = cascade;
    }


    public String getOrder() {
        return order;
    }

    public void setOrder(String order) {
        this.order = order;
    }
    public String getFetch() {
        return fetch;
    }

    public void setFetch(String fetch) {
        this.fetch = fetch;
    }
    public String getCollection() {
        return collection;
    }

    public void setCollection(String collection) {
        this.collection = collection;
    }
    public String getCascade() {
        return cascade;
    }

    public void setCascade(String cascade) {
        this.cascade = cascade;
    }


}