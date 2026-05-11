





import java.util.List;
import java.util.ArrayList;

public class gast_types_Member extends SourceEntity {

    private boolean virtual;
    private boolean internal;
    private String visibility;
    private boolean abstract;
    private boolean typeParameterClassMember;
    private boolean final;
    private boolean override;
    private boolean introspectable;
    private boolean extern;
    private boolean static;



    public gast_types_Member(
        boolean virtual,        boolean internal,        String visibility,        boolean abstract,        boolean typeParameterClassMember,        boolean final,        boolean override,        boolean introspectable,        boolean extern,        boolean static    ) {
        super(
        );
        this.virtual = virtual;
        this.internal = internal;
        this.visibility = visibility;
        this.abstract = abstract;
        this.typeParameterClassMember = typeParameterClassMember;
        this.final = final;
        this.override = override;
        this.introspectable = introspectable;
        this.extern = extern;
        this.static = static;
    }


    public boolean getVirtual() {
        return virtual;
    }

    public void setVirtual(boolean virtual) {
        this.virtual = virtual;
    }
    public boolean getInternal() {
        return internal;
    }

    public void setInternal(boolean internal) {
        this.internal = internal;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public boolean getTypeparameterclassmember() {
        return typeParameterClassMember;
    }

    public void setTypeparameterclassmember(boolean typeParameterClassMember) {
        this.typeParameterClassMember = typeParameterClassMember;
    }
    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }
    public boolean getOverride() {
        return override;
    }

    public void setOverride(boolean override) {
        this.override = override;
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
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }


}