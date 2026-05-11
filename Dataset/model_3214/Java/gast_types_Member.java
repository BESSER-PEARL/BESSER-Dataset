





import java.util.List;
import java.util.ArrayList;

public class gast_types_Member extends SourceEntity {

    private boolean final;
    private boolean virtual;
    private boolean typeParameterClassMember;
    private boolean static;
    private boolean internal;
    private boolean extern;
    private boolean abstract;
    private boolean introspectable;
    private boolean override;
    private String visibility;



    public gast_types_Member(
        boolean final,        boolean virtual,        boolean typeParameterClassMember,        boolean static,        boolean internal,        boolean extern,        boolean abstract,        boolean introspectable,        boolean override,        String visibility    ) {
        super(
        );
        this.final = final;
        this.virtual = virtual;
        this.typeParameterClassMember = typeParameterClassMember;
        this.static = static;
        this.internal = internal;
        this.extern = extern;
        this.abstract = abstract;
        this.introspectable = introspectable;
        this.override = override;
        this.visibility = visibility;
    }


    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }
    public boolean getVirtual() {
        return virtual;
    }

    public void setVirtual(boolean virtual) {
        this.virtual = virtual;
    }
    public boolean getTypeparameterclassmember() {
        return typeParameterClassMember;
    }

    public void setTypeparameterclassmember(boolean typeParameterClassMember) {
        this.typeParameterClassMember = typeParameterClassMember;
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
    public boolean getExtern() {
        return extern;
    }

    public void setExtern(boolean extern) {
        this.extern = extern;
    }
    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public boolean getIntrospectable() {
        return introspectable;
    }

    public void setIntrospectable(boolean introspectable) {
        this.introspectable = introspectable;
    }
    public boolean getOverride() {
        return override;
    }

    public void setOverride(boolean override) {
        this.override = override;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }


}