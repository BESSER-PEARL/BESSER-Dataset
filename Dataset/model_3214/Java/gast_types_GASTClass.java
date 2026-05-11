





import java.util.List;
import java.util.ArrayList;

public class gast_types_GASTClass extends types_GASTType, types_Member {

    private boolean local;
    private boolean anonymous;
    private boolean inner;
    private boolean primitive;
    private boolean interface;
    private int linesOfComments;





    private List<GASTClass> gastclasss;




    private List<GASTClass> gastclasss;




    private Package package;




    private List<Access> accesss;




    private GASTClass gastclass;




    private GASTClass gastclass;




    private List<GASTClass> gastclasss;




    private List<GASTClass> gastclasss;




    private List<Function> functions;




    private List<TypeAlias> typealiass;




    private Function function;




    private List<Delegate> delegates;


    public gast_types_GASTClass(
        boolean local,        boolean anonymous,        boolean inner,        boolean primitive,        boolean interface,        int linesOfComments    ) {
        super(
        );
        this.local = local;
        this.anonymous = anonymous;
        this.inner = inner;
        this.primitive = primitive;
        this.interface = interface;
        this.linesOfComments = linesOfComments;
        this.gastclasss = new ArrayList<>();
        this.gastclasss = new ArrayList<>();
        this.accesss = new ArrayList<>();
        this.gastclasss = new ArrayList<>();
        this.gastclasss = new ArrayList<>();
        this.functions = new ArrayList<>();
        this.typealiass = new ArrayList<>();
        this.delegates = new ArrayList<>();
    }

    public gast_types_GASTClass(
        boolean local,        boolean anonymous,        boolean inner,        boolean primitive,        boolean interface,        int linesOfComments        ArrayList<GASTClass> gastclasss,        ArrayList<GASTClass> gastclasss,        ArrayList<Access> accesss,        ArrayList<GASTClass> gastclasss,        ArrayList<GASTClass> gastclasss,        ArrayList<Function> functions,        ArrayList<TypeAlias> typealiass,        ArrayList<Delegate> delegates    ) {
        this.local = local;
        this.anonymous = anonymous;
        this.inner = inner;
        this.primitive = primitive;
        this.interface = interface;
        this.linesOfComments = linesOfComments;
        this.gastclasss = gastclasss;
        this.gastclasss = gastclasss;
        this.accesss = accesss;
        this.gastclasss = gastclasss;
        this.gastclasss = gastclasss;
        this.functions = functions;
        this.typealiass = typealiass;
        this.delegates = delegates;
    }

    public boolean getLocal() {
        return local;
    }

    public void setLocal(boolean local) {
        this.local = local;
    }
    public boolean getAnonymous() {
        return anonymous;
    }

    public void setAnonymous(boolean anonymous) {
        this.anonymous = anonymous;
    }
    public boolean getInner() {
        return inner;
    }

    public void setInner(boolean inner) {
        this.inner = inner;
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
    public int getLinesofcomments() {
        return linesOfComments;
    }

    public void setLinesofcomments(int linesOfComments) {
        this.linesOfComments = linesOfComments;
    }

    public List<GASTClass> getGastclasss() {
        return gastclasss;
    }

    public void addGastclass(Gastclass gastclass) {
        this.gastclasss.add(gastclass);
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
    public List<Access> getAccesss() {
        return accesss;
    }

    public void addAccess(Access access) {
        this.accesss.add(access);
    }
    public GASTClass getGastclass() {
        return gastclass;
    }

    public void setGastclass(GASTClass gastclass) {
        this.gastclass = gastclass;
    }
    public GASTClass getGastclass() {
        return gastclass;
    }

    public void setGastclass(GASTClass gastclass) {
        this.gastclass = gastclass;
    }
    public List<GASTClass> getGastclasss() {
        return gastclasss;
    }

    public void addGastclass(Gastclass gastclass) {
        this.gastclasss.add(gastclass);
    }
    public List<GASTClass> getGastclasss() {
        return gastclasss;
    }

    public void addGastclass(Gastclass gastclass) {
        this.gastclasss.add(gastclass);
    }
    public List<Function> getFunctions() {
        return functions;
    }

    public void addFunction(Function function) {
        this.functions.add(function);
    }
    public List<TypeAlias> getTypealiass() {
        return typealiass;
    }

    public void addTypealias(Typealias typealias) {
        this.typealiass.add(typealias);
    }
    public Function getFunction() {
        return function;
    }

    public void setFunction(Function function) {
        this.function = function;
    }
    public List<Delegate> getDelegates() {
        return delegates;
    }

    public void addDelegate(Delegate delegate) {
        this.delegates.add(delegate);
    }

}