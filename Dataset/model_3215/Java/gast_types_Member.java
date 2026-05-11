





import java.util.List;
import java.util.ArrayList;

public class gast_types_Member extends SourceEntity {

    private boolean override;
    private boolean final;
    private String visibility;
    private boolean static;
    private boolean extern;
    private boolean abstract;
    private boolean virtual;
    private boolean internal;
    private boolean introspectable;
    private boolean typeParameterClassMember;



    public gast_types_Member(
        boolean override,        boolean final,        String visibility,        boolean static,        boolean extern,        boolean abstract,        boolean virtual,        boolean internal,        boolean introspectable,        boolean typeParameterClassMember    ) {
        super(
        );
        this.override = override;
        this.final = final;
        this.visibility = visibility;
        this.static = static;
        this.extern = extern;
        this.abstract = abstract;
        this.virtual = virtual;
        this.internal = internal;
        this.introspectable = introspectable;
        this.typeParameterClassMember = typeParameterClassMember;
    }


    public boolean getOverride() {
        return override;
    }

    public void setOverride(boolean override) {
        this.override = override;
    }
    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
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
    public boolean getIntrospectable() {
        return introspectable;
    }

    public void setIntrospectable(boolean introspectable) {
        this.introspectable = introspectable;
    }
    public boolean getTypeparameterclassmember() {
        return typeParameterClassMember;
    }

    public void setTypeparameterclassmember(boolean typeParameterClassMember) {
        this.typeParameterClassMember = typeParameterClassMember;
    }


}