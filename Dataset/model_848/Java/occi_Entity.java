





import java.util.List;
import java.util.ArrayList;

public class occi_Entity  {

    private String location;
    private String id;
    private String title;





    private occi_Kind occi_kind;




    private List<occi_Mixin> occi_mixins;




    private List<occi_MixinBase> occi_mixinbases;




    private occi_MixinBase occi_mixinbase;




    private List<occi_AttributeState> occi_attributestates;




    private occi_Mixin occi_mixin;




    private occi_Kind occi_kind;


    public occi_Entity(
        String location,        String id,        String title    ) {
        this.location = location;
        this.id = id;
        this.title = title;
        this.occi_mixins = new ArrayList<>();
        this.occi_mixinbases = new ArrayList<>();
        this.occi_attributestates = new ArrayList<>();
    }

    public occi_Entity(
        String location,        String id,        String title        ArrayList<occi_Mixin> occi_mixins,        ArrayList<occi_MixinBase> occi_mixinbases,        ArrayList<occi_AttributeState> occi_attributestates    ) {
        this.location = location;
        this.id = id;
        this.title = title;
        this.occi_mixins = occi_mixins;
        this.occi_mixinbases = occi_mixinbases;
        this.occi_attributestates = occi_attributestates;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public occi_Kind getOcci_kind() {
        return occi_kind;
    }

    public void setOcci_kind(occi_Kind occi_kind) {
        this.occi_kind = occi_kind;
    }
    public List<occi_Mixin> getOcci_mixins() {
        return occi_mixins;
    }

    public void addOcci_mixin(Occi_mixin occi_mixin) {
        this.occi_mixins.add(occi_mixin);
    }
    public List<occi_MixinBase> getOcci_mixinbases() {
        return occi_mixinbases;
    }

    public void addOcci_mixinbase(Occi_mixinbase occi_mixinbase) {
        this.occi_mixinbases.add(occi_mixinbase);
    }
    public occi_MixinBase getOcci_mixinbase() {
        return occi_mixinbase;
    }

    public void setOcci_mixinbase(occi_MixinBase occi_mixinbase) {
        this.occi_mixinbase = occi_mixinbase;
    }
    public List<occi_AttributeState> getOcci_attributestates() {
        return occi_attributestates;
    }

    public void addOcci_attributestate(Occi_attributestate occi_attributestate) {
        this.occi_attributestates.add(occi_attributestate);
    }
    public occi_Mixin getOcci_mixin() {
        return occi_mixin;
    }

    public void setOcci_mixin(occi_Mixin occi_mixin) {
        this.occi_mixin = occi_mixin;
    }
    public occi_Kind getOcci_kind() {
        return occi_kind;
    }

    public void setOcci_kind(occi_Kind occi_kind) {
        this.occi_kind = occi_kind;
    }

}