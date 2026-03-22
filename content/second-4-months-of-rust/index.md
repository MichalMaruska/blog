---
title: "Second 4 months of Rust"
date: 2026-01-28
draft: false
---

# Second 4 months of Rust

## Macros

## CLAP

## Using Clippy

## Std...

Reading the pages .....traits defined, Enums, Structs .... and (generic) definitions of the trait for EXTERNAL types. That's why it's listed there, not in the page of those types.

**Any** .....using

intrinsics::type\_id::<T>()

## HashMap ...

## [Tricking the HashMap | Ivan Dubrov](https://idubrov.name/rust/2018/06/01/tricking-the-hashmap.html)

## 

## !Sized

Generics parameters implicitly constrained to Sized

## - iterators

## -

## Error handling

Option -> Result

[std::Result]( https://doc.rust-lang.org/std/result/enum.Result.html)

? expands to ..... return Err(From::from(e))

### Defining new error types out of lower-level ones:

[YT: Mastering Error Handling in Rust: From Panics to thiserror & anyhow | with Nathan Stocks](https://www.youtube.com/watch?v=sZV6sz4P6QY)

#[non\_exhaustive]

thiserror   ->

> #[derive(Error)]

      #[error("message")]

      ....#[from:] ...

and we can use  [derive\_more::Error](https://docs.rs/derive_more/latest/derive_more/)

[Error trait](https://doc.rust-lang.org/core/error/trait.Error.html) enables the nesting:

* source()
* provide()   default to None, but can be implemented

[YT: A Simpler Way to See Results](https://www.youtube.com/watch?v=s5S2Ed5T-dc)

Anyhow:

<https://docs.rs/anyhow/latest/anyhow/index.html>

[thiserror](https://github.com/dtolnay/thiserror):  derive macro to have custom error and transformation from other Error types.

#### Clarifying references with  Claude.io:

https://doc.rust-lang.org/std/primitive.reference.html

Prompts:

Rust references implement all certain traits Copy, Clone etc ..... is it because those traits have only &self methods?  
.....    
Yes,true. Those specific Traits are implemented by the definition/semantics of References.  What I meant is the other Traits which .... references having Deref... when implemented for T and containing only &self methods, are therefore implemented for &T.  Or is there anything more profound on that?

Now I know:

> A trait being callable through &T doesn't mean &T implements that trait in the type system's eyes.
