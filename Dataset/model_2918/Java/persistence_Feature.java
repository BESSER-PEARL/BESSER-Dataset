





import java.util.List;
import java.util.ArrayList;

public class persistence_Feature  {

    private boolean collectionOrmAllowRemove;
    private String displayClass;
    private String nullDisplayValue;
    private String footerClass;
    private String title;
    private boolean encodeUriKey;
    private String headerClass;
    private boolean collectionOrmAllowAdd;
    private String placeholder;





    private List<persistence_SerializationGroup> persistence_serializationgroups;




    private persistence_EntityOrView persistence_entityorview;




    private persistence_EntityOrView persistence_entityorview;




    private persistence_EntityOrView persistence_entityorview;




    private persistence_EntityOrView persistence_entityorview;




    private persistence_EntityOrView persistence_entityorview;


    public persistence_Feature(
        boolean collectionOrmAllowRemove,        String displayClass,        String nullDisplayValue,        String footerClass,        String title,        boolean encodeUriKey,        String headerClass,        boolean collectionOrmAllowAdd,        String placeholder    ) {
        this.collectionOrmAllowRemove = collectionOrmAllowRemove;
        this.displayClass = displayClass;
        this.nullDisplayValue = nullDisplayValue;
        this.footerClass = footerClass;
        this.title = title;
        this.encodeUriKey = encodeUriKey;
        this.headerClass = headerClass;
        this.collectionOrmAllowAdd = collectionOrmAllowAdd;
        this.placeholder = placeholder;
        this.persistence_serializationgroups = new ArrayList<>();
    }

    public persistence_Feature(
        boolean collectionOrmAllowRemove,        String displayClass,        String nullDisplayValue,        String footerClass,        String title,        boolean encodeUriKey,        String headerClass,        boolean collectionOrmAllowAdd,        String placeholder        ArrayList<persistence_SerializationGroup> persistence_serializationgroups    ) {
        this.collectionOrmAllowRemove = collectionOrmAllowRemove;
        this.displayClass = displayClass;
        this.nullDisplayValue = nullDisplayValue;
        this.footerClass = footerClass;
        this.title = title;
        this.encodeUriKey = encodeUriKey;
        this.headerClass = headerClass;
        this.collectionOrmAllowAdd = collectionOrmAllowAdd;
        this.placeholder = placeholder;
        this.persistence_serializationgroups = persistence_serializationgroups;
    }

    public boolean getCollectionormallowremove() {
        return collectionOrmAllowRemove;
    }

    public void setCollectionormallowremove(boolean collectionOrmAllowRemove) {
        this.collectionOrmAllowRemove = collectionOrmAllowRemove;
    }
    public String getDisplayclass() {
        return displayClass;
    }

    public void setDisplayclass(String displayClass) {
        this.displayClass = displayClass;
    }
    public String getNulldisplayvalue() {
        return nullDisplayValue;
    }

    public void setNulldisplayvalue(String nullDisplayValue) {
        this.nullDisplayValue = nullDisplayValue;
    }
    public String getFooterclass() {
        return footerClass;
    }

    public void setFooterclass(String footerClass) {
        this.footerClass = footerClass;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public boolean getEncodeurikey() {
        return encodeUriKey;
    }

    public void setEncodeurikey(boolean encodeUriKey) {
        this.encodeUriKey = encodeUriKey;
    }
    public String getHeaderclass() {
        return headerClass;
    }

    public void setHeaderclass(String headerClass) {
        this.headerClass = headerClass;
    }
    public boolean getCollectionormallowadd() {
        return collectionOrmAllowAdd;
    }

    public void setCollectionormallowadd(boolean collectionOrmAllowAdd) {
        this.collectionOrmAllowAdd = collectionOrmAllowAdd;
    }
    public String getPlaceholder() {
        return placeholder;
    }

    public void setPlaceholder(String placeholder) {
        this.placeholder = placeholder;
    }

    public List<persistence_SerializationGroup> getPersistence_serializationgroups() {
        return persistence_serializationgroups;
    }

    public void addPersistence_serializationgroup(Persistence_serializationgroup persistence_serializationgroup) {
        this.persistence_serializationgroups.add(persistence_serializationgroup);
    }
    public persistence_EntityOrView getPersistence_entityorview() {
        return persistence_entityorview;
    }

    public void setPersistence_entityorview(persistence_EntityOrView persistence_entityorview) {
        this.persistence_entityorview = persistence_entityorview;
    }
    public persistence_EntityOrView getPersistence_entityorview() {
        return persistence_entityorview;
    }

    public void setPersistence_entityorview(persistence_EntityOrView persistence_entityorview) {
        this.persistence_entityorview = persistence_entityorview;
    }
    public persistence_EntityOrView getPersistence_entityorview() {
        return persistence_entityorview;
    }

    public void setPersistence_entityorview(persistence_EntityOrView persistence_entityorview) {
        this.persistence_entityorview = persistence_entityorview;
    }
    public persistence_EntityOrView getPersistence_entityorview() {
        return persistence_entityorview;
    }

    public void setPersistence_entityorview(persistence_EntityOrView persistence_entityorview) {
        this.persistence_entityorview = persistence_entityorview;
    }
    public persistence_EntityOrView getPersistence_entityorview() {
        return persistence_entityorview;
    }

    public void setPersistence_entityorview(persistence_EntityOrView persistence_entityorview) {
        this.persistence_entityorview = persistence_entityorview;
    }

}