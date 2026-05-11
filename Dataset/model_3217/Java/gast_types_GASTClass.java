





import java.util.List;
import java.util.ArrayList;

public class gast_types_GASTClass extends types_Member, types_GASTType {

    private boolean primitive;
    private boolean interface;
    private boolean inner;
    private int linesOfComments;
    private boolean anonymous;
    private boolean local;





    private List<GASTClass> gastclasss;




    private Package package;




    private List<Function> functions;




    private List<GASTClass> gastclasss;




    private List<TypeAlias> typealiass;




    private List<Access> accesss;




    private List<GASTClass> gastclasss;




    private GASTClass gastclass;




    private List<Delegate> delegates;




    private List<GASTClass> gastclasss;




    private GASTClass gastclass;




    private Function function;


    public gast_types_GASTClass(
        boolean primitive,        boolean interface,        boolean inner,        int linesOfComments,        boolean anonymous,        boolean local    ) {
        super(
        );
        this.primitive = primitive;
        this.interface = interface;
        this.inner = inner;
        this.linesOfComments = linesOfComments;
        this.anonymous = anonymous;
        this.local = local;
        this.gastclasss = new ArrayList<>();
        this.functions = new ArrayList<>();
        this.gastclasss = new ArrayList<>();
        this.typealiass = new ArrayList<>();
        this.accesss = new ArrayList<>();
        this.gastclasss = new ArrayList<>();
        this.delegates = new ArrayList<>();
        this.gastclasss = new ArrayList<>();
    }

    public gast_types_GASTClass(
        boolean primitive,        boolean interface,        boolean inner,        int linesOfComments,        boolean anonymous,        boolean local        ArrayList<GASTClass> gastclasss,        ArrayList<Function> functions,        ArrayList<GASTClass> gastclasss,        ArrayList<TypeAlias> typealiass,        ArrayList<Access> accesss,        ArrayList<GASTClass> gastclasss,        ArrayList<Delegate> delegates,        ArrayList<GASTClass> gastclasss    ) {
        this.primitive = primitive;
        this.interface = interface;
        this.inner = inner;
        this.linesOfComments = linesOfComments;
        this.anonymous = anonymous;
        this.local = local;
        this.gastclasss = gastclasss;
        this.functions = functions;
        this.gastclasss = gastclasss;
        this.typealiass = typealiass;
        this.accesss = accesss;
        this.gastclasss = gastclasss;
        this.delegates = delegates;
        this.gastclasss = gastclasss;
    }

    public boolean getPrimitive() {
        return primitive;
    }

    public void setPrimitive(boolean primitive) {
        this.primitive = primitive;
    }
    public boolean getInterface() {
        return interface;
    }

    public void setInterface(boolean interface) {
        this.interface = interface;
    }
    public boolean getInner() {
        return inner;
    }

    public void setInner(boolean inner) {
        this.inner = inner;
    }
    public int getLinesofcomments() {
        return linesOfComments;
    }

    public void setLinesofcomments(int linesOfComments) {
        this.linesOfComments = linesOfComments;
    }
    public boolean getAnonymous() {
        return anonymous;
    }

    public void setAnonymous(boolean anonymous) {
        this.anonymous = anonymous;
    }
    public boolean getLocal() {
        return local;
    }

    public void setLocal(boolean local) {
        this.local = local;
    }

    public List<GASTClass> getGastclasss() {
        return gastclasss;
    }

    public void addGastclass(Gastclass gastclass) {
        this.gastclasss.add(gastclass);
    }
    public Package getPackage() {
        return package;
    }

    public void setPackage(Package package) {
        this.package = package;
    }
    public List<Function> getFunctions() {
        return functions;
    }

    public void addFunction(Function function) {
        this.functions.add(function);
    }
    public List<GASTClass> getGastclasss() {
        return gastclasss;
    }

    public void addGastclass(Gastclass gastclass) {
        this.gastclasss.add(gastclass);
    }
    public List<TypeAlias> getTypealiass() {
        return typealiass;
    }

    public void addTypealias(Typealias typealias) {
        this.typealiass.add(typealias);
    }
    public List<Access> getAccesss() {
        return accesss;
    }

    public void addAccess(Access access) {
        this.accesss.add(access);
    }
    public List<GASTClass> getGastclasss() {
        return gastclasss;
    }

    public void addGastclass(Gastclass gastclass) {
        this.gastclasss.add(gastclass);
    }
    public GASTClass getGastclass() {
        return gastclass;
    }

    public void setGastclass(GASTClass gastclass) {
        this.gastclass = gastclass;
    }
    public List<Delegate> getDelegates() {
        return delegates;
    }

    public void addDelegate(Delegate delegate) {
        this.delegates.add(delegate);
    }
    public List<GASTClass> getGastclasss() {
        return gastclasss;
    }

    public void addGastclass(Gastclass gastclass) {
        this.gastclasss.add(gastclass);
    }
    public GASTClass getGastclass() {
        return gastclass;
    }

    public void setGastclass(GASTClass gastclass) {
        this.gastclass = gastclass;
    }
    public Function getFunction() {
        return function;
    }

    public void setFunction(Function function) {
        this.function = function;
    }

}