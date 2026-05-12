





import java.util.List;
import java.util.ArrayList;

public class IResolver  {






    private build_context_IBuildContext build_context_ibuildcontext;




    private build_resolver_ResolverGroup build_resolver_resolvergroup;


    public IResolver(
    ) {
    }



    public build_context_IBuildContext getBuild_context_ibuildcontext() {
        return build_context_ibuildcontext;
    }

    public void setBuild_context_ibuildcontext(build_context_IBuildContext build_context_ibuildcontext) {
        this.build_context_ibuildcontext = build_context_ibuildcontext;
    }
    public build_resolver_ResolverGroup getBuild_resolver_resolvergroup() {
        return build_resolver_resolvergroup;
    }

    public void setBuild_resolver_resolvergroup(build_resolver_ResolverGroup build_resolver_resolvergroup) {
        this.build_resolver_resolvergroup = build_resolver_resolvergroup;
    }

}