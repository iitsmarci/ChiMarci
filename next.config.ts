import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // @ts-ignore - Next.js types might not be updated for this config
  allowedDevOrigins: ["192.168.1.81"],
};

export default nextConfig;
