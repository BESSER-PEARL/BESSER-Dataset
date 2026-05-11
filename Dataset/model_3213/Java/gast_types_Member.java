





import java.util.List;
import java.util.ArrayList;

public class gast_types_Member extends SourceEntity {

    private boolean static;
    private boolean internal;
    private boolean abstract;
    private boolean final;
    private boolean introspectable;
    private boolean extern;
    private boolean override;
    private boolean typeParameterClassMember;
    private String visibility;
    private boolean virtual;



    public gast_types_Member(
        boolean static,        boolean internal,        boolean abstract,        boolean final,        boolean introspectable,        boolean extern,        boolean override,        boolean typeParameterClassMember,        String visibility,        boolean virtual    ) {
        super(
        );
        this.static = static;
        this.internal = internal;
        this.abstract = abstract;
        this.final = final;
        this.introspectable = introspectable;
        this.extern = extern;
        this.override = override;
        this.typeParameterClassMember = typeParameterClassMember;
        this.visibility = visibility;
        this.virtual = virtual;
    }


    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public boolean getInternal() {
        return internal;
    }

    public void setInternal(boolean internal) {
        this.internal = internal;
    }
    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }
    public boolean getIntrospectable() {
        return introspectable;
    }

    public void setIntrospectable(boolean introspectable) {
        this.introspectable = introspectable;
    }
    public boolean getExtern() {
        return extern;
    }

    public void setExtern(boolean extern) {
        this.extern = extern;
    }
    public boolean getOverride() {
        return override;
    }

    public void setOverride(boolean override) {
        this.override = override;
    }
    public boolean getTypeparameterclassmember() {
        return typeParameterClassMember;
    }

    public void setTypeparameterclassmember(boolean typeParameterClassMember) {
        this.typeParameterClassMember = typeParameterClassMember;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public boolean getVirtual() {
        return virtual;
    }

    public void setVirtual(boolean virtual) {
        this.virtual = virtual;
    }


}