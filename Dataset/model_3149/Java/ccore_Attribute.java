





import java.util.List;
import java.util.ArrayList;

public class ccore_Attribute extends EAttribute, Item {

    private boolean hiddenInComputedPages;
    private boolean isList;
    private String tWEvol;
    private boolean mustBeInitialized;
    private boolean require;
    private boolean tWRevSpecific;
    private String idRuntime;
    private String tWUpdateKind;
    private boolean natif;
    private boolean cannotBeUndefined;
    private String tWCommitKind;
    private boolean devGenerated;
    private boolean _final;





    private ccore_TypeDefinition ccore_typedefinition;


    public ccore_Attribute(
        boolean hiddenInComputedPages,        boolean isList,        String tWEvol,        boolean mustBeInitialized,        boolean require,        boolean tWRevSpecific,        String idRuntime,        String tWUpdateKind,        boolean natif,        boolean cannotBeUndefined,        String tWCommitKind,        boolean devGenerated,        boolean _final    ) {
        super(
        );
        this.hiddenInComputedPages = hiddenInComputedPages;
        this.isList = isList;
        this.tWEvol = tWEvol;
        this.mustBeInitialized = mustBeInitialized;
        this.require = require;
        this.tWRevSpecific = tWRevSpecific;
        this.idRuntime = idRuntime;
        this.tWUpdateKind = tWUpdateKind;
        this.natif = natif;
        this.cannotBeUndefined = cannotBeUndefined;
        this.tWCommitKind = tWCommitKind;
        this.devGenerated = devGenerated;
        this._final = _final;
    }


    public boolean getHiddenincomputedpages() {
        return hiddenInComputedPages;
    }

    public void setHiddenincomputedpages(boolean hiddenInComputedPages) {
        this.hiddenInComputedPages = hiddenInComputedPages;
    }
    public boolean getIslist() {
        return isList;
    }

    public void setIslist(boolean isList) {
        this.isList = isList;
    }
    public String getTwevol() {
        return tWEvol;
    }

    public void setTwevol(String tWEvol) {
        this.tWEvol = tWEvol;
    }
    public boolean getMustbeinitialized() {
        return mustBeInitialized;
    }

    public void setMustbeinitialized(boolean mustBeInitialized) {
        this.mustBeInitialized = mustBeInitialized;
    }
    public boolean getRequire() {
        return require;
    }

    public void setRequire(boolean require) {
        this.require = require;
    }
    public boolean getTwrevspecific() {
        return tWRevSpecific;
    }

    public void setTwrevspecific(boolean tWRevSpecific) {
        this.tWRevSpecific = tWRevSpecific;
    }
    public String getIdruntime() {
        return idRuntime;
    }

    public void setIdruntime(String idRuntime) {
        this.idRuntime = idRuntime;
    }
    public String getTwupdatekind() {
        return tWUpdateKind;
    }

    public void setTwupdatekind(String tWUpdateKind) {
        this.tWUpdateKind = tWUpdateKind;
    }
    public boolean getNatif() {
        return natif;
    }

    public void setNatif(boolean natif) {
        this.natif = natif;
    }
    public boolean getCannotbeundefined() {
        return cannotBeUndefined;
    }

    public void setCannotbeundefined(boolean cannotBeUndefined) {
        this.cannotBeUndefined = cannotBeUndefined;
    }
    public String getTwcommitkind() {
        return tWCommitKind;
    }

    public void setTwcommitkind(String tWCommitKind) {
        this.tWCommitKind = tWCommitKind;
    }
    public boolean getDevgenerated() {
        return devGenerated;
    }

    public void setDevgenerated(boolean devGenerated) {
        this.devGenerated = devGenerated;
    }
    public boolean get_final() {
        return _final;
    }

    public void set_final(boolean _final) {
        this._final = _final;
    }

    public ccore_TypeDefinition getCcore_typedefinition() {
        return ccore_typedefinition;
    }

    public void setCcore_typedefinition(ccore_TypeDefinition ccore_typedefinition) {
        this.ccore_typedefinition = ccore_typedefinition;
    }

}